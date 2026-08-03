## ACID propriedades e Time Travel
## Inserindo dados na tabela Iceberg
spark.sql("INSERT INTO iceberg.curso.despachantes VALUES (11,'Carlos Silva', 'Ativo','Curitiba',4200,'2026-02-10')")

spark.sql("SELECT * FROM iceberg.curso.despachantes").show()

## Consultando snapshots da tabela Iceberg
spark.sql("SELECT * FROM iceberg.curso.despachantes.snapshots").show()

## Realizando update na tabela Iceberg
spark.sql("UPDATE iceberg.curso.despachantes SET vendas = 9999 WHERE id=1")

spark.sql("SELECT * FROM iceberg.curso.despachantes").show()

## Deletando dados na tabela Iceberg
spark.sql("DELETE FROM iceberg.curso.despachantes WHERE id=11")

spark.sql("SELECT * FROM iceberg.curso.despachantes").show()

spark.sql("SELECT * FROM iceberg.curso.despachantes.snapshots").show()

## Consultando dados da tabela Iceberg em um snapshot específico
spark.sql("SELECT * FROM iceberg.curso.despachantes VERSION AS OF 2460570787034542950").show()

spark.sql("SELECT * FROM iceberg.curso.despachantes VERSION AS OF 6475094813477983619").show()