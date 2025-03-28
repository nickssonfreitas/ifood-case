from pyspark.sql.functions import col, when, mean
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, isnan, when, lit


def isna_sum(df: DataFrame, name: str) -> None:
    """
    Exibe o schema, total de linhas e contagem de nulos + percentual por coluna.

    Parâmetros:
        df (DataFrame): DataFrame do Spark
        name (str): Nome para exibição
    """
    total_rows = df.count()

    print(f"\n📘 Schema de {name}:")
    df.printSchema()

    print(f"\n🔢 Total de linhas: {total_rows}")

    print(f"\n📊 Nulos por coluna (valores e %):")

    nulls_df = df.select([
        count(when(col(c).isNull() | isnan(c), c)).alias(c)
        for c in df.columns
    ])

    # Converte o resultado de uma linha para um formato coluna/valor
    for row in nulls_df.collect():
        for col_name in df.columns:
            null_count = row[col_name]
            null_percent = (null_count / total_rows) * 100 if total_rows else 0
            print(f"– {col_name}: {null_count} nulos ({null_percent:.2f}%)")

    print(f"\n🔎 Amostra de {name}:")
    df.show(5, truncate=False)


def value_counts(df: DataFrame, column: str, show_nulls=True) -> None:
    """
    Exibe a contagem e porcentagem de cada valor único em uma coluna.

    Parâmetros:
        df (DataFrame): o DataFrame do Spark
        column (str): o nome da coluna a ser analisada
        show_nulls (bool): se True, inclui valores nulos na contagem
    """
    total = df.count()

    # Cria nova coluna temporária com valor "NULL" para facilitar agrupamento
    col_expr = when(col(column).isNull(), "NULL").otherwise(
        col(column)) if show_nulls else col(column)

    print(f"\n📊 Distribuição da coluna: {column} (total: {total} registros)")

    df.groupBy(col_expr.alias(column)) \
      .agg(
          count("*").alias("count"),
          (count("*") / lit(total) * 100).alias("percent")
    ) \
        .orderBy("count", ascending=False) \
        .show(truncate=False)

