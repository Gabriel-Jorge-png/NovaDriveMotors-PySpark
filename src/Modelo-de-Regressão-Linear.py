## Importando as bibliotecas necessárias
from pyspark.ml.regression import LinearRegression

from pyspark.ml.feature import VectorAssembler

from pyspark.ml import Pipeline

##Criando o DF com os dados da tabela carros
carros_temp = spark.read.csv("/app/data/Carros.csv", inferSchema=True, header=True, sep=";")
                                                                                
carros_temp.show(5)

## Filtrando apenas as colunas que serão utilizadas no modelo de regressão
carros = carros_temp.select("Consumo", "Cilindros", "Cilindradas", "HP")

carros.show(5)

## Criando o vetor de características | OBS: ESSA ETAPA É SÓ PARA MOSTRAR COMO FUNCIONA, POIS O VETOR DE CARACTERÍSTICAS SERÁ CRIADO DENTRO DO PIPELINE
veccaracteristicas = VectorAssembler(inputCols=["Consumo","Cilindros","Cilindradas"],outputCol="caracteristicas")

## Transformando o DF carros em um vetor de características
vec_carros = veccaracteristicas.transform(carros)

vec_carros.show(5)

## Criando o modelo de regressão linear
reglin = LinearRegression(featuresCol="caracteristicas", labelCol="HP")

## Criando o pipeline com as etapas de transformação e o modelo de regressão
pipeline = Pipeline(stages=[veccaracteristicas, reglin])

## Treinando o modelo de regressão linear com o pipeline
pipeline_model = pipeline.fit(carros)

## Fazendo a previsão com o modelo treinado
previsao = pipeline_model.transform(carros)

In [20]: previsao.show(5)

## Avaliando o modelo de regressão linear
from pyspark.sql.functions import abs, col

avaliacao = previsao.withColumn("erro_absoluto", abs(col("HP") - col("prediction")))

avaliacao.show(5)

## Calculando o erro médio absoluto
from pyspark.sql.functions import avg

avaliacao.select(avg("erro_absoluto").alias("erro_medio_absoluto")).show()
