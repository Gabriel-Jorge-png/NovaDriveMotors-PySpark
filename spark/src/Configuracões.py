## Mostrando a configuração atual do Spark para o número de partições de shuffle
spark.conf.get("spark.sql.suffle.partitions")

## Alterando a configuração do Spark para o número de partições de shuffle para 8
In [14]: spark.conf.set("spark.sql.suffle.partitions","8")

## Mostrando a configuração atual do Spark para o número de partições de shuffle após a alteração
In [15]: spark.conf.get("spark.sql.suffle.partitions")

## Configuração valida apenas para a sessão atual do Spark. Se o Spark for reiniciado, a configuração voltará ao valor padrão.