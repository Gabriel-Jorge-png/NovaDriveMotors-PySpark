## Adicionando uma nova coluna na tabela Iceberg
spark.sql("ALTER TABLE iceberg.curso.despachantes ADD COLUMN comissao DOUBLE")

## Consultando metadados da tabela Iceberg
spark.sql("DESCRIBE TABLE iceberg.curso.despachantes").show()

## Atualizando a coluna comissao calculando 10% do valor da coluna vendas
spark.sql("UPDATE iceberg.curso.despachantes SET comissao = vendas * 0.1")

spark.sql("SELECT * FROM iceberg.curso.despachantes").show()

## Consultando snapshots da tabela Iceberg
spark.sql("SELECT * FROM iceberg.curso.despachantes.snapshots").show()

## Consultando dados da tabela Iceberg em um snapshot específico
spark.sql("SELECT * FROM iceberg.curso.despachantes VERSION AS OF 6996631905356328841").show()