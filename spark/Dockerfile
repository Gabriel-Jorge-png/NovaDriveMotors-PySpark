FROM spark:3.5.6

USER root

RUN mkdir -p /opt/spark/jars-extra

ADD https://jdbc.postgresql.org/download/postgresql-42.7.9.jar /opt/spark/jars-extra/postgresql-42.7.9.jar

RUN chmod 644 /opt/spark/jars-extra/postgresql-42.7.9.jar

RUN pip install ipython pandas

ENV SPARK_EXTRA_CLASSPATH=/opt/spark/jars-extra/postgresql-42.7.9.jar

USER spark