

# GOT TO THIS LINK https://kafka.apache.org/quickstart FOR HOW TO:
    # START ZOOKEEPER AND KAFKA SERVER
    # CREATE A KAFKA TOPIC


# IMPORT KAFKA DEPENDENCIES

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.4.0,org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 pyspark-shell'

# IMPORT PYSPARK
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split


# CREATE SPARK SESSION
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("StructuredStreaming_Kafka_wordcount2") \
    .getOrCreate()

# CREATE A STREAMING DATAFRAME
lines = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test_kafka") \
    .load()


words = lines.select(explode(split(lines.value, " ")).alias("word"))


wordCounts = words.groupBy("word").count()  # THIS IS THE AGGREGATION/QUERY WE WANT SPARK TO APPLY ON KAFKA STREAM


# NOW SEND SOME MESSAGES WITH A PRODUCER (TOPIC: test_kafka)
# FOR HOW TO: STEP 4 OF KAFKA QUICKSTART LINK

query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()


query.awaitTermination()

# COMPLETE FORMAT ONLY WORKS IF THERE'S AN AGGREGATION. FOR OTHER FORMATS GO TO: https://jaceklaskowski.gitbooks.io/spark-structured-streaming/spark-sql-streaming-OutputMode.html
# RUN THIS AND START TYPING IN THE PRODUCER TERMINAL

query.stop()
