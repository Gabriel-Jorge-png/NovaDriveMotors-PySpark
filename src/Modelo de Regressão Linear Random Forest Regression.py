## Importando as bibliotecas necessárias
from pyspark.ml.regression import LinearRegression, RandomForestRegressor

from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.ml.feature import VectorAssembler

## Criando o DF com os dados da tabela carros
carros_temp = spark.read.csv("/app/data/Carros.csv", header=False, sep=";")
                                                                                
carros_temp.show()

## Friltrando apenas as colunas que serão utilizadas no modelo de regressão
carros_temp = spark.read.csv("/app/data/Carros.csv",inferSchema=True, header=True, sep=";")
                                                                                
carros_temp.show()

## Filtrando apenas as colunas que serão utilizadas no modelo de regressão
carros = carros_temp.select("Consumo","Cilindros","Cilindradas","HP")

carros.show(5)

## Criando o vetor de características
veccaracteristicas = VectorAssembler(inputCols=["Consumo","Cilindros","Cilindradas"],outputCol="caracteristicas")

## Transformando o DF carros em um vetor de características
carros = veccaracteristicas.transform(carros)

carros.show(truncate=False)

## Dividindo o DF carros em treino e teste
carros_treino, carros_teste = carros.randomSplit([0.7,0.3], seed=42)

carros_treino.count()

carros_teste.count()

## Criando o modelo de regressão linear
reglin = LinearRegression(featuresCol="caracteristicas", labelCol="HP")

## Treinando o modelo de regressão linear
modelo_reglin = reglin.fit(carros_treino)

## Fazendo a previsão com o modelo treinado
previsao_reglin = modelo_reglin.transform(carros_teste)

previsao_reglin.show(truncate=False)

## Avaliando o modelo de regressão linear
avaliador = RegressionEvaluator(predictionCol="prediction", labelCol="HP", metricName="rmse")

## Calculando o RMSE do modelo de regressão linear
rmse_reglin = avaliador.evaluate(previsao_reglin)

rmse_reglin

## Criando o modelo de regressão Random Forest
rfreg = RandomForestRegressor(featuresCol="caracteristicas", labelCol="HP", seed=42)

## Treinando o modelo de regressão Random Forest
modelo_rf = rfreg.fit(carros_treino)

## Fazendo a previsão com o modelo treinado
previsao_rf = modelo_rf.transform(carros_teste)

previsao_rf.show(truncate=False)

## Avaliando o modelo de regressão Random Forest
In [40]: rmse_rf = avaliador.evaluate(precisao_rf)

## Calculando o RMSE do modelo de regressão Random Forest e comparando com o RMSE do modelo de regressão linear
rmse_rf

rmse_reglin