import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.4.0,org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 pyspark-shell'


from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("StructuredStreaming_Kafka_age") \
    .getOrCreate()

#######

df = spark \
    .readStream \
    .format('kafka') \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "persons") \
    .option("startingOffsets", "earliest") \
    .load()

out_df = df.writeStream \
    .outputMode('append') \
    .format("console") \
    .start()

personJSONdf= df.selectExpr("CAST(value AS STRING)")

out_JSON_df = personJSONdf.writeStream \
    .outputMode('append') \
    .format("console") \
    .start()


schema = StructType().add("age", StringType()).add("id", StringType()).add("first_name", StringType()).add("last_name", StringType()).add("email", StringType()).add("gender", StringType()).add("ip_address", StringType())


personNestedDF = personJSONdf.select(from_json(col('value').cast('string'), schema).alias('person'))
personNestedDF.printSchema()

out_nested_df = personNestedDF.writeStream \
    .outputMode('append') \
    .format("console") \
    .start()







#######
schema = StructType().add("age", StringType()).add("id", StringType()).add("first_name", StringType()).add("last_name", StringType()).add("email", StringType()).add("gender", StringType()).add("ip_address", StringType())



df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "persons") \
    .option("startingOffsets", "earliest") \
    .load() \
    .select(from_json(col('value').cast('string'), schema).alias('person')) \
    .selectExpr("cast (person.age as integer)", "cast (person.id as integer)", "person.first_name", "person.last_name", "person.email", "person.gender", "person.ip_address")

df.printSchema()

transform = df.filter("age > 25")
transform = transform.groupBy('id').agg(sum('age'))


query = transform \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

#######

transform = df.select("id", "age", "gender").where("age > 25").filter("gender = 'Female'")


transform \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()


#######
df.writeStream \
  .format("console") \
  .start()


