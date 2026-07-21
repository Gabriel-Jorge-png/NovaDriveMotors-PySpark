from pyspark.sql import SparkSession
import os

if __name__ == "__main__":  
    spark = SparkSession.builder.appName("Aplicação Ler Postgres").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")

    url = f"jdbc:postgresql://{host}:{port}/{db}"

    veiculos = (
    spark.read.format("jdbc")
    .option("url",url)
    .option("dbtable","veiculos")
    .option("user",user)
    .option("password",password)
    .option("driver","org.postgresql.Driver")
    .load()
    )

    veiculos.write.mode("overwrite").parquet("/app/output/veiculos_parquet")

    spark.stop()

    ## para executar o script com parâmetros, use o seguinte comando:
    ## spark-submit (.\run.ps1) apps/Transformacao_parametros.py --input /app/data/despachantes.csv --output /app/output/vendas_por_ano