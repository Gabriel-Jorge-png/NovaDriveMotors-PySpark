## Configurações do Streaming
jsonschema = "nome STRING, postagem STRING, data INT"

entrada = "/app/data/streaming/posts"

saida = "/app/output/posts_parquet"

## Leitura do Stream
df = spark.readStream.json(entrada,schema=jsonschema)

df.printSchema()

## Escrita do Stream
consulta = (
    df.writeStream
    .format("parquet")
    .outputMode("append")
    .trigger(processingTime = "5 seconds")
    .option("path",saida)
    .option("checkpointLocation","/app/output/checkpoints/posts_parquet")
    .start()
    )

## Aguardar a finalização do Stream (Atualiza a cada 5 segundos), ctrl + c para finalizar
consulta.awaitTermination()

## Leitura do arquivo Parquet
post = spark.read.parquet("/app/output/posts_parquet")

In [19]: post.show()

In [20]: post.count()