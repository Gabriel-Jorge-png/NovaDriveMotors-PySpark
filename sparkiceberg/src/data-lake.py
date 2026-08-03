## Criando um data lake com Apache Iceberg e Spark

## Carregando os dados do data lake em formato Parquet e salvando-os em dataframes Spark
clientes = spark.read.parquet("/app/data/Clientes.parquet")
                                                                                
produtos = spark.read.parquet("/app/data/Produtos.parquet")

vendas = spark.read.parquet("/app/data/Vendas.parquet")

vendedores = spark.read.parquet("/app/data/Vendedores.parquet")

itensvendas = spark.read.parquet("/app/data/ItensVendas.parquet")

clientes.show(5)

## Criando tabelas Iceberg a partir dos dataframes Spark e salvando-as no data lake
clientes.writeTo("iceberg.datalake.clientes").create()
                                                                                
produtos.writeTo("iceberg.datalake.produtos").create()

vendedores.writeTo("iceberg.datalake.vendedores").create()

vendas.writeTo("iceberg.datalake.vendas").create()

itensvendas.writeTo("iceberg.datalake.itensvendas").create()

## Consultando as tabelas do data lake
spark.sql("SHOW TABLES IN iceberg.datalake").show()

## Consultando metadados da tabela Iceberg
spark.sql("DESCRIBE TABLE iceberg.datalake.vendas").show()

## Consultando os snapshots da tabela Iceberg
spark.sql("SELECT * FROM iceberg.datalake.vendas.snapshots").show()

## Consultando os dados da tabela Iceberg
spark.sql("SELECT * FROM iceberg.datalake.clientes LIMIT 10").show()

## Consultando os dados da tabela Iceberg com SQL realizando um join entre as tabelas clientes e vendas, agrupando por cliente e ordenando pelo total vendido
spark.sql("""
    ...: SELECT
    ...:     c.clienteID,
    ...:     c.cliente,
    ...:     COUNT(v.VendasID) as Qtdevendas,
    ...:     SUM(v.Total) as TotalVendido
    ...: FROM iceberg.datalake.clientes c
    ...: JOIN iceberg.datalake.vendas v on c.clienteID = v.clienteID
    ...: GROUP BY c.clienteID, c.Cliente
    ...: ORDER BY TotalVendido
    ...: """).show()

## Snapshots, Time Travel e Rollback

## consultando os dados da tabela Iceberg antes de realizar o delete
spark.sql("SELECT *FROM iceberg.datalake.itensvendas WHERE vendasID = 1").show()

spark.sql("SELECT * FROM iceberg.datalake.vendas.snapshots").show()

## realizando o delete de um registro da tabela Iceberg
spark.sql("DELETE FROM iceberg.datalake.itensvendas WHERE vendasID = 1").show()

## consultando os dados da tabela Iceberg após realizar o delete
spark.sql("SELECT * FROM iceberg.datalake.itensvendas.snapshots").show()

## realizando o rollback da tabela Iceberg para o snapshot anterior ao delete
spark.sql("CALL iceberg.system.rollback_to_snapshot('datalake.itensvendas',5692244523824484397)").show()

## consultando os dados da tabela Iceberg após realizar o rollback
spark.sql("SELECT *FROM iceberg.datalake.itensvendas WHERE vendasID = 1").show()
