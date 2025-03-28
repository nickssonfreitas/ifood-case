from pyspark.sql import DataFrame
from pyspark.sql.functions import explode, col, lit, when, array_contains,  coalesce
from pyspark.sql.types import ArrayType, StructType, MapType, StringType, DoubleType
from pyspark.sql import DataFrame
from pyspark.sql import DataFrame
from pyspark.sql.functions import coalesce, col

def drop_columns(df: DataFrame, columns_to_drop: list[str]) -> DataFrame:
    """
    Remove uma lista de colunas de um DataFrame PySpark.

    Parâmetros:
    -----------
    df : DataFrame
        DataFrame de entrada.

    columns_to_drop : list of str
        Lista com os nomes das colunas que devem ser removidas.

    Retorno:
    --------
    DataFrame
        Novo DataFrame sem as colunas especificadas.
    """
    return df.drop(*columns_to_drop)

def consolidate_columns(df: DataFrame, output_col: str, input_cols: list[str]) -> DataFrame:
    """
    Cria uma nova coluna consolidada com base nos primeiros valores não nulos entre múltiplas colunas.

    Parâmetros:
    -----------
    df : DataFrame
        O DataFrame de entrada.
    
    output_col : str
        Nome da nova coluna de saída que conterá o valor consolidado.
    
    input_cols : list of str
        Lista de nomes das colunas candidatas, ordenadas por prioridade (primeiro valor não nulo será usado).

    Retorno:
    --------
    DataFrame
        DataFrame com a nova coluna `output_col` criada.
    """
    return df.withColumn(output_col, coalesce(*[col(c) for c in input_cols]))


def explode_list_columns_to_ohe(df: DataFrame, prefix_sep: str = "_") -> DataFrame:
    """
    Converte automaticamente colunas de lista (ArrayType) e dicionários (StructType ou MapType)
    em colunas expandidas. Remove as colunas originais após conversão.

    Parâmetros:
    -----------
    df : DataFrame
        DataFrame do PySpark contendo colunas complexas (arrays ou structs)
    prefix_sep : str
        Separador entre nome da coluna original e campo/valor (ex: 'value_offer_id')

    Retorno:
    --------
    DataFrame
        DataFrame transformado com colunas expandidas
    """
    transformed_df = df

    for field in df.schema.fields:
        col_name = field.name
        col_type = field.dataType

        # Tratamento de listas
        if isinstance(col_type, ArrayType):
            # Obter valores únicos da lista
            unique_values = (
                df.select(explode(col(col_name)).alias("item"))
                .distinct()
                .rdd.flatMap(lambda x: x)
                .collect()
            )

            # Criar colunas binárias
            for val in unique_values:
                new_col = f"{col_name}{prefix_sep}{val}"
                transformed_df = transformed_df.withColumn(
                    new_col,
                    when(array_contains(col(col_name), val), lit(1)).otherwise(0)
                )

            # Remove a coluna original
            transformed_df = transformed_df.drop(col_name)

        # Tratamento de dicionários (struct ou map)
        elif isinstance(col_type, (StructType, MapType)):
            for subfield in col_type.names if isinstance(col_type, StructType) else df.select(col_name).schema[0].dataType.keyType:
                new_col = f"{col_name}{prefix_sep}{subfield}"
                transformed_df = transformed_df.withColumn(new_col, col(col_name)[subfield])

            # Remove a coluna original
            transformed_df = transformed_df.drop(col_name)

    return transformed_df

def integrate_all_dataframes(
    transactions_df: DataFrame,
    customers_df: DataFrame,
    offers_df: DataFrame
) -> DataFrame:
    """
    Integra transações com dados de clientes e ofertas em uma tabela única.

    Parâmetros:
    -----------
    transactions_df : DataFrame
        Contém eventos como 'transaction', 'offer received', etc.
    
    customers_df : DataFrame
        Informações de clientes. Chave: id
    
    offers_df : DataFrame
        Metadados das ofertas. Chave: id

    Retorno:
    --------
    DataFrame
        Tabela única contendo eventos enriquecidos com dados do cliente e da oferta.
    """

    # 1️⃣ Join transactions + customers
    df_joined = transactions_df.join(
        customers_df,
        transactions_df.account_id == customers_df.id,
        how="left"
    ).drop(customers_df.id)

    # 2️⃣ Join com offers
    df_final = df_joined.join(
        offers_df,
        df_joined.offer_id == offers_df.id,
        how="left"
    ).drop(offers_df.id)

    return df_final
