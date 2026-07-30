## Importando as bibliotecas necessárias
from pyspark.ml.feature import RFormula

from pyspark.ml.classification import NaiveBayes

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

## Criando o DF com os dados da tabela iris
iris = spark.read.csv("/app/data/iris.csv", inferSchema=True, header=True)
                                                                                
iris.show(5)

## Criando o vetor de características e a coluna de label
formula = RFormula(formula="class ~ .", featuresCol="features", labelCol="label", handleInvalid="skip")

iris_trans = formula.fit(iris).transform(iris).select("features","label")
                                                                                
iris_trans.show(5)

## Dividindo o DF iris_trans em treino e teste
iris_treino, iris_teste = iris_trans.randomSplit([0.7,0.3], seed=42)

iris_treino.count()

iris_teste.count()

## Criando o modelo de classificação Naive Bayes
nb = NaiveBayes(labelCol="label", featuresCol="features")

## Treinando o modelo de classificação Naive Bayes
modelo = nb.fit(iris_treino)

## Fazendo a previsão com o modelo treinado                                
previsao = modelo.transform(iris_teste)

previsao.show()

previsao.show(truncate=False)

## Avaliando o modelo de classificação Naive Bayes
avaliador = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="label", metricName="accuracy")

## Calculando a acurácia do modelo de classificação Naive Bayes
accuracy = avaliador.evaluate(previsao)
                                                                                
accuracy