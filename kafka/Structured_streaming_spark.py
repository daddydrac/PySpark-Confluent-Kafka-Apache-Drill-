

# Structured streaming vs. Spark Streaming:
# Structured streaming is a newer, highly optimized API for Spark. Spark streaming is older/original RDD based streaming

# STRUCTURED STREAMING:
# structured streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
# spark SQL engine updates the final result as streaming data continues to arrive.
# you can use the dataset/dataframe API to express streaming aggregations, event-time windows, stream-to-batch joins etc.

# the key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended
# every data item that is arriving on the stream is like a new row being appended to the input table.
# This leads to a new stream processing model that is very similar to batch processing model.
# You will express your streaming computation as standard batch-like query as on a static table

# an example: a streaming word count:

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

# create dataframe representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()



# split the lines into words:

words = lines.select(explode(split(lines.value, " ")).alias("word"))  # word is the new column name created with alias

# generate running word count:

wordCounts = words.groupBy('word').count()

# we have now set up the query on the streaming data. All that is left is to actually start receiving data and computing counts
# To do this, we set it up to print the complete set of counts (specified by outputMode('complete')) to the console every time they are updated
# and then start the streaming computation using start().

# the lines dataframe is the input table, and wordCounts dataframe is the result table

# Start running the query that prints the running counts to the console

# open a terminal and type nc -lk 9999
query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
# now start typing on the terminal


# after this code is executed, the streaming computation will have started in the background.
# the query object is a handle to that active streaming query,
# and we have decided to wait for the termination of the query using awaitTermination() to prevent the process from
# exiting while the query is active.

# the outputMode can be defined in a different mode:
    # complete mode: the entire updated Result Table will be written to the external storage.
    # append mode: only the news appended in the Result Table since the last trugger will be written to the external storage
    # update mode: only the rows that were updated in the result table since the last trigger will be written to the external storage



# CREATING STREAMING DATAFRAMES AND STREAMING DATASETS:

# INPUT SOURCES:

    # File sources: Reads file written in a directory as a stream of data.
    # Kafka source: reads data from kafka. compatible with kafka broker version 0.10.0 or higher
    # socket source: (test only) reads utf8 text data from a socket connection.
    # rate source: (test only) generates data at the specified number of rows per second, each output row contains a timestamp and value (value=message count)


