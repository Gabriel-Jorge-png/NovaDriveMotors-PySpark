from pyspark.sql import SparkSession
from pyspark.sql.functions import year
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aplicação com arquivos de entrada e saída")
    parser.add_argument("--input", required=True, help="Caminho entrada")
    parser.add_argument("--output", required=True, help="Caminho saída")
    args = parser.parse_args()

    spark = SparkSession.builder.appName("Aplicação Transformacao com Parametros").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    schema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"

    despachantes = spark.read.csv(args.input, header=False, schema=schema)

    resultado = despachantes.select("data").groupBy(year("data").alias("ano")).count()
    resultado.write.mode("overwrite").parquet(args.output)
    spark.stop()

    ## para executar o script com parâmetros, use o seguinte comando:
    ## spark-submit (.\run.ps1) apps/Transformacao_parametros.py --input /app/data/despachantes.csv --output /app/output/vendas_por_ano