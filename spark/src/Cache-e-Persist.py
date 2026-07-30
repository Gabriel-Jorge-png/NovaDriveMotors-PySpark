## Criando um DataFrame de vendas, clientes e vendedores
vendas_completas = (
     vendas
     .join(clientes, "ClienteID")
     .join(vendedores, "VendedorID")
)

## Caching o DataFrame de vendas e clientes
vendas_completas.cache()

vendas_completas.count()                                                                    

vendas_completas.groupBy("Estado").sum("Total").show()

## Unpersisting o DataFrame de vendas e clientes
vendas_completas.unpersist()

## Importando a classe StorageLevel do PySpark
from pyspark import StorageLevel

## Criando um DataFrame de vendas e clientes
vendas_clientes = (
     vendas
     .join(clientes, "ClienteID")
     .filter("Total > 100")
)

## Persistindo o DataFrame de vendas e clientes
vendas_clientes.persist(StorageLevel.MEMORY_AND_DISK)

vendas_clientes.count()

vendas_clientes.groupBy("Estado").sum("Total").show()

vendas_clientes.unpersist()