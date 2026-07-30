from pyspark.sql import SparkSession
from pyspark.sql.functions import year

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Aplicação Transformacao").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    schema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"

    despachantes = spark.read.csv("/app/data/despachantes.csv", header=False, schema=schema)

    resultado = despachantes.select("data").groupBy(year("data").alias("ano")).count()
    resultado.write.mode("overwrite").parquet("/app/output/vendas_por_ano")
    spark.stop()

    ### para executar o script com parâmetros, use o seguinte comando:
    ### spark-submit (.\run.ps1) Transformacao.py