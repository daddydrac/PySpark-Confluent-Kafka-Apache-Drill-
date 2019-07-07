import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.4.0,org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 pyspark-shell'


from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("SS_kafka_csv") \
    .getOrCreate()

# read from csv
mySchema = StructType().add("id", IntegerType()).add("name", StringType()).add("year", IntegerType()).add("rating", DoubleType()).add("duration", IntegerType())

streamingDataFrame = spark.readStream.schema(mySchema).csv("/Users/nevinyilmaz/Desktop/moviedata.csv")

streamingDataFrame.printSchema()

# publish it to kafka

streamingDataFrame.selectExpr("CAST(id AS STRING) AS key") \
    .writeStream \
    .format("kafka") \
    .option("topic", "topic_csv") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("startingOffsets", "earliest")\
    .start()

spark.conf.set("spark.sql.streaming.checkpointLocation", "/Users/nevinyilmaz/Desktop")