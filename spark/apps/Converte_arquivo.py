from pyspark.sql import SparkSession
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aplicação que converte arquivo")
    parser.add_argument("-t","--tipo", required=True,choices=["parquet","json", "csv","orc"], help="Tipo de arquivo")
    parser.add_argument("-i","--input", required=True, help="Caminho do csv")
    parser.add_argument("-o","--output", required=True, help="Diretório de saída")
    args = parser.parse_args()

    spark = SparkSession.builder.appName("Aplicação de Conversão de Arquivos").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    dados = spark.read.csv(args.input, header=False, inferSchema=True)
    dados.write.mode("overwrite").format(args.tipo).save(args.output)
    spark.stop()

    ## para executar o script com parâmetros, use o seguinte comando:
    ## spark-submit (.\run.ps1) apps/Transformacao_parametros.py --input /app/data/despachantes.csv --output /app/output/vendas_por_ano