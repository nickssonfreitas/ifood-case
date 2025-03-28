from pyspark.sql import SparkSession

def create_spark_session(app_name: str = "iFood - Data Processing", log_level: str = "WARN") -> SparkSession:
    """
    Cria uma SparkSession com configurações padrão para leitura local.

    Parâmetros:
    -----------
    app_name : str
        Nome da aplicação Spark (exibido no UI do Spark)
    log_level : str
        Nível de log do Spark. Ex: "WARN", "INFO", "ERROR", "DEBUG"

    Retorno:
    --------
    SparkSession
        Instância da SparkSession configurada
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

    spark.sparkContext.setLogLevel(log_level)
    print(f"✅ SparkSession iniciada com sucesso com nível de log '{log_level}'!")
    return spark
