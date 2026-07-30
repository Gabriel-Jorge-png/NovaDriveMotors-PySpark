print(vendas.rdd.getNumPartitions())
1

print(itens.rdd.getNumPartitions())
1

## Criando uma nova partição com 8 partições
vendas2 = vendas.repartition(8)

print(vendas.rdd.getNumPartitions())
1

print(vendas2.rdd.getNumPartitions())
8

## Diminuindo o número de partições para 1
vendas3 = vendas2.coalesce(1)

print(vendas3.rdd.getNumPartitions())

## Particionamento geralmente é usado para melhorar a performance de operações de leitura e escrita, enquanto o coalesce é usado para reduzir o número de partições, geralmente após uma operação que aumentou o número de partições desnecessariamente causando overhead operacional.