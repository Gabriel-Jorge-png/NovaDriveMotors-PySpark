## Importando as bibliotecas necessárias
from pyspark.ml.feature import RFormula

from pyspark.ml.classification import DecisionTreeClassifier

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

## Criando o DF com os dados da tabela churn
churn = spark.read.csv("/app/data/Churn.csv", inferSchema=True, header=True, sep=":")
                                                                                
churn.show(3)

## Criando o DF com os dados da tabela churn
spark.read.csv("/app/data/Churn.csv", inferSchema=True, header=True, sep=";")

churn.show(3)

## Criando o vetor de características e a coluna de label
formula = RFormula(formula="Exited ~ .", featuresCol="features", labelCol="label", handleInvalid="skip")

## Transformando o DF churn em um vetor de características e a coluna de label
churn_trans = formula.fit(churn).transform(churn).select("features","label")
                                                                                
churn_trans.show(truncate=False)

## Contando a quantidade de registros por classe
churn_trans.groupBy("label").count().show()

## Balanceamento de classes
classe_0 = churn_trans.filter("label = 0.0")

classe_1 = churn_trans.filter("label = 1.0")

qtd_classe_0 = classe_0.count()

qtd_classe_1 = classe_1.count()

## Calculando a fração de registros da classe 1 em relação à classe 0
qtd_classe_0


qtd_classe_1

## Calculando a fração de registros da classe 1 em relação à classe 0
fracao_classe_0 = qtd_classe_1 / qtd_classe_0

fracao_classe_0

## Balanceando a classe 0 para que tenha a mesma quantidade de registros da classe 1
classe_0_balanceada = classe_0.sample(withReplacement=False,fraction=fracao_classe_0, seed=42)

## Verificando a quantidade de registros por classe após o balanceamento
churn_balanceado = classe_0_balanceada.union(classe_1)

churn_balanceado.groupBy("label").count().show()

## Dividindo o DF churn_balanceado em treino e teste
churn_treino, churn_teste = churn_balanceado.randomSplit([0.7,0.3], seed=42)

churn_treino.count()

churn_teste.count()

## Verificando a quantidade de registros por classe no DF de treino e teste
churn_treino.groupBy("label").count().show()

churn_teste.groupBy("label").count().show()

## Criando o modelo de classificação Decision Tree
dt = DecisionTreeClassifier(labelCol="label", featuresCol="features", seed=42)

## Treinando o modelo de classificação Decision Tree
modelo = dt.fit(churn_treino)

## Fazendo a previsão com o modelo treinado
previsao = modelo.transform(churn_teste)

previsao.show(truncate=False)

## Avaliando o modelo de classificação Decision Tree
avaliador_acc = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="label", metricName="accuracy")

accuracy = avaliador_acc.evaluate(previsao)

accuracy