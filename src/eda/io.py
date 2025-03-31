def save_spark_dataframe(
    df,
    path: str,
    format: str = "parquet",
    mode: str = "overwrite",
    compression: str = "snappy"
) -> None:
    """
    Salva um DataFrame do Spark em disco.

    Parâmetros:
    -----------
    df : DataFrame
        DataFrame do Spark a ser salvo.
    path : str
        Caminho de destino (diretório ou arquivo).
    format : str
        Formato de salvamento: 'parquet', 'csv', 'json'. Default = 'parquet'.
    mode : str
        Modo de escrita: 'overwrite', 'append', 'ignore', 'error'. Default = 'overwrite'.
    compression : str
        Tipo de compressão: 'gzip', 'snappy', 'none' (depende do formato). Default = 'snappy'.
    """
    print(f"💾 Salvando dados em: {path} (formato: {format}, compressão: {compression})")
    df.write \
      .format(format) \
      .mode(mode) \
      .option("compression", compression) \
      .save(path)
    print("✅ Dados salvos com sucesso.")


def read_spark_dataframe(
    spark,
    path: str,
    format: str = "parquet",
    infer_schema: bool = True,
    header: bool = True
):
    """
    Lê um DataFrame do Spark a partir de arquivos salvos.

    Parâmetros:
    -----------
    spark : SparkSession
        Sessão Spark ativa.
    path : str
        Caminho de leitura (diretório ou arquivo).
    format : str
        Formato de leitura: 'parquet', 'csv', 'json'. Default = 'parquet'.
    infer_schema : bool
        Se True, tenta inferir o schema automaticamente (para CSV/JSON). Default = True.
    header : bool
        Se True, usa a primeira linha como header (para CSV). Default = True.

    Retorno:
    --------
    DataFrame
        DataFrame do Spark carregado.
    """
    print(f"📂 Lendo dados de: {path} (formato: {format})")
    reader = spark.read.format(format)
    
    if format in ["csv", "json"]:
        reader = reader.option("inferSchema", infer_schema).option("header", header)

    df = reader.load(path)
    print("✅ Leitura concluída.")
    return df