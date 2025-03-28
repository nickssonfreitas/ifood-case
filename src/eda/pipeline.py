from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when, mean, year, to_date

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_date, year, when


def feature_engineering_customers_data(df: DataFrame) -> DataFrame:
    """
    Realiza engenharia de atributos no DataFrame de clientes.

    Cria:
    - 'birth_year': ano de nascimento com base em 'registered_on' e 'age'
    - 'age_group': categorização geracional com faixa etária estimada
    - 'credit_limit_bucket': discretização do limite do cartão de crédito

    Faixas do limite de crédito:
    -----------------------------
    - Low (≤ 10k)
    - Medium (10k–30k)
    - High (30k–60k)
    - Very High (> 60k)

    Parâmetros:
    -----------
    df : DataFrame
        DataFrame do PySpark com colunas:
        - age (int)
        - registered_on (yyyyMMdd)
        - credit_card_limit (float)

    Retorno:
    --------
    DataFrame com as colunas 'birth_year', 'age_group' e 'credit_limit_bucket'
    """

    # Cálculo do ano de nascimento
    df = df.withColumn(
        "birth_year",
        year(to_date(col("registered_on").cast("string"), "yyyyMMdd")) - col("age")
    )

    # Categorização de faixa etária
    df = df.withColumn(
        "age_group",
        when(col("birth_year") <= 1964, "Boomers (60+)")
        .when((col("birth_year") >= 1965) & (col("birth_year") <= 1979), "Gen X (45–59)")
        .when((col("birth_year") >= 1980) & (col("birth_year") <= 1994), "Millennials (30–44)")
        .when((col("birth_year") >= 1995) & (col("birth_year") <= 2009), "Gen Z (15–29)")
        .when(col("birth_year") >= 2010, "Gen Alpha (<15)")
        .otherwise("Unknown")
    )

    # Faixa de limite do cartão de crédito
    df = df.withColumn(
        "credit_limit_bucket",
        when(col("credit_card_limit") <= 10000, "Low (≤ 10k)")
        .when((col("credit_card_limit") > 10000) & (col("credit_card_limit") <= 30000), "Medium (10k–30k)")
        .when((col("credit_card_limit") > 30000) & (col("credit_card_limit") <= 60000), "High (30k–60k)")
        .when(col("credit_card_limit") > 60000, "Very High (> 60k)")
        .otherwise("Unknown")
    )

    return df


def clean_customers_data(df: DataFrame) -> DataFrame:
    """
    Cleans the 'gender' and 'credit_card_limit' columns in the customers dataset.

    Cleaning rules:
    - 'gender':
        - Keep 'M' and 'F'
        - Replace 'O' and NULL with 'unknown'
    - 'credit_card_limit':
        - Replace NULLs with the median value of the column

    Parameters:
        df (DataFrame): Input Spark DataFrame with raw customer data

    Returns:
        DataFrame: Cleaned DataFrame
    """

    print("🔍 Cleaning 'gender' column...")
    df = df.withColumn(
        "gender",
        when(col("gender").isin("M", "F"), col("gender")).otherwise("unknown")
    )
    print("✅ 'gender' cleaned: values normalized (M, F, unknown)")

    print("\n📈 Calculating statistics for 'credit_card_limit'...")

    # Mean (optional debug/info)
    mean_value = df.select(mean("credit_card_limit")).first()[0]
    print(f"📊 Mean credit limit: {mean_value:.2f}")

    # Median via approxQuantile
    median_value = df.approxQuantile("credit_card_limit", [0.5], 0.01)[0]
    print(f"📏 Median credit limit: {median_value:.2f}")

    # Fill NULLs with median
    df = df.fillna({"credit_card_limit": median_value})
    print("✅ 'credit_card_limit' nulls filled with median.")

    return df
