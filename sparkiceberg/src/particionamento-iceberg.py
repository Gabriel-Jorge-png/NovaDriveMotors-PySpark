## Criando tabela particionada no Iceberg
spark.sql("CREATE TABLE iceberg.curso.despachantes_part USING ICEBERG PARTITIONED BY (cidade) AS SELECT * FROM iceberg.curso.despachantes")

spark.sql("SELECT cidade, count(*) total FROM iceberg.curso.despachantes_part GROUP BY cidade").show()

## Consultando arquivos da tabela particionada no Iceberg
spark.sql("SELECT file_path, partition FROM iceberg.curso.despachantes_part.files").show()

spark.sql("SELECT file_path, partition FROM iceberg.curso.despachantes_part.files").show(truncate=False)