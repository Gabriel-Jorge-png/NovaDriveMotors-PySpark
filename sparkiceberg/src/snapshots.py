## Criando catálogo e tabela no Iceberg
arqschema = "id STRING, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"

spark.read.csv("/app/data/despachantes.csv", header=False, schema=arqschema)

df.show()

## Criando namespace e tabela no Iceberg
spark.sql("CREATE NAMESPACE IF NOT EXISTS iceberg.curso")

df.writeTo("iceberg.curso.despachantes").createOrReplace()

spark.sql("SELECT * FROM iceberg.curso.despachantes").show()

spark.sql("SHOW NAMESPACES IN iceberg").show()

spark.sql("SHOW TABLES IN iceberg.curso").show()

## Consultando metadados da tabela Iceberg
spark.sql("DESCRIBE iceberg.curso.despachantes").show()

spark.sql("DESCRIBE EXTENDED iceberg.curso.despachantes").show()

spark.sql("DESCRIBE EXTENDED iceberg.curso.despachantes").show(truncate=False)

## Consultando snapshots da tabela Iceberg
spark.sql("SELECT * FROM iceberg.curso.despachantes.snapshots").show(truncate=False)

spark.sql("SELECT * FROM iceberg.curso.despachantes.snapshots").show()