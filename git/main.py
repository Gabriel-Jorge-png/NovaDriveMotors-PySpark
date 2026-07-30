from flask import Flask

app = Flask(__name__)

## Importando pacote OS
import os

## Definindo os acessos
host = os.getenv("POSTGRES_HOST")

host
'159.223.187.110'

port = os.getenv("POSTGRES_PORT")

port
'5432'

db = os.getenv("POSTGRES_DB")

db
'novadrive'

user = os.getenv("POSTGRES_USER")

user
'etlreadonly'

password = os.getenv("POSTGRES_PASSWORD")

password
'novadrive376A@'

url = f"jdbc:postgresql://{host}:{port}/{db}"

url
'jdbc:postgresql://159.223.187.110:5432:novadrive'

df = (
spark.read.format("jdbc")
.option("url",url)
.option("dbtable","public.veiculos")
.option("user",user)
.option("password",password)
.option("driver","org.postgresql.Driver")
.load()
)

df.show()
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|id_veiculos|          nome|                tipo|    valor|    data_atualizacao|       data_inclusao|
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|          1|  AgileXplorer|        SUV Compacta|250000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          2|  VoyageRoamer|           SUV Média|350000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          3|   EcoPrestige| SUV Premium Híbrida|500000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          4|    WorkMaster|     Camionete Média|280000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          5|    DoubleDuty|Camionete Cabine ...|320000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          6|     SpeedFury|      Superesportivo|800000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          7|TrailConqueror|            Off-road|400000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          8| ElegantCruise|                Sedã|300000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
+-----------+--------------+--------------------+---------+--------------------+--------------------+

## Função para ler outras tabelas
def ler_postgresql(tabela):
             return(
                 spark.read
                 .format("jdbc")
                 .option("url",url)
                 .option("dbtable",tabela)
                 .option("user",user)
                 .option("password",password)
                 .option("driver","org.postgresql.Driver")
                 .load()
     )
    

estados = ler_postgresql("public.estados")

estados.show()
+----------+-------------------+-----+--------------------+--------------------+
|id_estados|             estado|sigla|       data_inclusao|    data_atualizacao|
+----------+-------------------+-----+--------------------+--------------------+
|         1|               Acre|   AC|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         2|            Alagoas|   AL|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         3|              Amapá|   AP|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         4|           Amazonas|   AM|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         5|              Bahia|   BA|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         6|              Ceará|   CE|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         7|   Distrito Federal|   DF|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         8|     Espírito Santo|   ES|2024-01-28 19:58:...|2024-01-28 19:58:...|
|         9|              Goiás|   GO|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        10|           Maranhão|   MA|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        11|        Mato Grosso|   MT|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        12| Mato Grosso do Sul|   MS|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        13|       Minas Gerais|   MG|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        14|               Pará|   PA|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        15|            Paraíba|   PB|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        16|             Paraná|   PR|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        17|         Pernambuco|   PE|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        18|              Piauí|   PI|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        19|     Rio de Janeiro|   RJ|2024-01-28 19:58:...|2024-01-28 19:58:...|
|        20|Rio Grande do Norte|   RN|2024-01-28 19:58:...|2024-01-28 19:58:...|
+----------+-------------------+-----+--------------------+--------------------+
only showing top 20 rows

veiculos = ler_postgresql("public.veiculos")

veiculos.show()
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|id_veiculos|          nome|                tipo|    valor|    data_atualizacao|       data_inclusao|
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|          1|  AgileXplorer|        SUV Compacta|250000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          2|  VoyageRoamer|           SUV Média|350000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          3|   EcoPrestige| SUV Premium Híbrida|500000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          4|    WorkMaster|     Camionete Média|280000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          5|    DoubleDuty|Camionete Cabine ...|320000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          6|     SpeedFury|      Superesportivo|800000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          7|TrailConqueror|            Off-road|400000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          8| ElegantCruise|                Sedã|300000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
+-----------+--------------+--------------------+---------+--------------------+--------------------+

## Criando uma Temp View
veiculos.createOrReplaceTempView("veiculos")

spark.sql("SELECT * FROM veiculos").show()
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|id_veiculos|          nome|                tipo|    valor|    data_atualizacao|       data_inclusao|
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|          1|  AgileXplorer|        SUV Compacta|250000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          2|  VoyageRoamer|           SUV Média|350000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          3|   EcoPrestige| SUV Premium Híbrida|500000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          4|    WorkMaster|     Camionete Média|280000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          5|    DoubleDuty|Camionete Cabine ...|320000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          6|     SpeedFury|      Superesportivo|800000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          7|TrailConqueror|            Off-road|400000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          8| ElegantCruise|                Sedã|300000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
+-----------+--------------+--------------------+---------+--------------------+--------------------+

## Usando a Temp View para fazer consultas
spark.sql("SELECT * FROM veiculos where valor > 30000").show()
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|id_veiculos|          nome|                tipo|    valor|    data_atualizacao|       data_inclusao|
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|          1|  AgileXplorer|        SUV Compacta|250000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          2|  VoyageRoamer|           SUV Média|350000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          3|   EcoPrestige| SUV Premium Híbrida|500000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          4|    WorkMaster|     Camionete Média|280000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          5|    DoubleDuty|Camionete Cabine ...|320000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          6|     SpeedFury|      Superesportivo|800000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          7|TrailConqueror|            Off-road|400000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          8| ElegantCruise|                Sedã|300000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
+-----------+--------------+--------------------+---------+--------------------+--------------------+

## Gerando uma consulta em um DF
veiculossql = (
    ...: spark.read.format("jdbc")
    ...: .option("url",url)
    ...: .option("query","select * from veiculos")
    ...: .option("user",user)
    ...: .option("password",password)
    ...: .option("driver","org.postgresql.Driver")
    ...: .load()
    ...: )

veiculossql.show()
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|id_veiculos|          nome|                tipo|    valor|    data_atualizacao|       data_inclusao|
+-----------+--------------+--------------------+---------+--------------------+--------------------+
|          1|  AgileXplorer|        SUV Compacta|250000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          2|  VoyageRoamer|           SUV Média|350000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          3|   EcoPrestige| SUV Premium Híbrida|500000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          4|    WorkMaster|     Camionete Média|280000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          5|    DoubleDuty|Camionete Cabine ...|320000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          6|     SpeedFury|      Superesportivo|800000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          7|TrailConqueror|            Off-road|400000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
|          8| ElegantCruise|                Sedã|300000.00|2024-01-28 19:58:...|2024-01-28 19:58:...|
+-----------+--------------+--------------------+---------+--------------------+--------------------+

