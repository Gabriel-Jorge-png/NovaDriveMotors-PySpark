## importando a função broadcast do PySpark
from pyspark.sql.functions import broadcast

spark.sql("USE vendasvarejo")

### Realizando o join entre as tabelas itens e produtos forçando o broadcast
join_broadcast = (
    ...:     itens
    ...:     .join(
    ...:         broadcast(produtos),
    ...:         itens.ProdutoID == produtos.ProdutoID,
    ...:         "inner"
    ...:     )
    ...: )

join_broadcast.show()

join_broadcast.explain()

## Broadcast geralmente é usado para melhorar a performance de operações de join, especialmente quando uma das tabelas é significativamente menor que a outra. Ao usar broadcast, a tabela menor é enviada para todos os nós do cluster, evitando o shuffle de dados e melhorando a eficiência do join.