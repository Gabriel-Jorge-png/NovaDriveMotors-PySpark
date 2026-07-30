## Criando o banco de dados otimizacao
spark.sql("CREATE DATABASE IF NOT EXISTS otimizacao")
26/07/26 16:54:07 WARN HiveConf: HiveConf of name hive.stats.jdbc.timeout does not exist
26/07/26 16:54:07 WARN HiveConf: HiveConf of name hive.stats.retries.wait does not exist
26/07/26 16:54:18 WARN ObjectStore: Version information not found in metastore. hive.metastore.schema.verification is not enabled so recording the schema version 2.3.0
26/07/26 16:54:18 WARN ObjectStore: setMetaStoreSchemaVersion called but recording version is disabled: version = 2.3.0, comment = Set by MetaStore UNKNOWN@172.18.0.2
26/07/26 16:54:19 WARN ObjectStore: Failed to get database otimizacao, returning NoSuchObjectException
26/07/26 16:54:19 WARN ObjectStore: Failed to get database otimizacao, returning NoSuchObjectException
26/07/26 16:54:19 WARN ObjectStore: Failed to get database global_temp, returning NoSuchObjectException
26/07/26 16:54:19 WARN ObjectStore: Failed to get database otimizacao, returning NoSuchObjectException
DataFrame[]

## Definindo o banco de dados otimizacao
spark.sql("USE otimizacao")

## Criando o dataframe de vendas e clientes
vendas = spark.read.parquet(("/app/data/Vendas.parquet"), header=True, schema=True)

clientes = spark.read.parquet(("/app/data/Clientes.parquet"), header=True, schema=True)

## Criando o bucket de vendas e clientes                                                                                
vendas.write.mode("overwrite").bucketBy(8,"ClienteID").sortBy("ClienteID").saveAsTable("vendas_bucket_cliente")

clientes.write.mode("overwrite").bucketBy(8,"ClienteID").sortBy("ClienteID").saveAsTable("clientes_bucket_cliente")

## Lendo os buckets de vendas e clientes
vendas_bucket = spark.table("vendas_bucket_cliente")

clientes_bucket = spark.table("clientes_bucket_cliente")

## Realizando o join entre os buckets de vendas e clientes
join_buckets = vendas_bucket.join(clientes_bucket, "ClienteID")

join_buckets.show()

## Explicando o plano de execução do join entre os buckets de vendas e clientes
In [13]: join_buckets.explain(True)