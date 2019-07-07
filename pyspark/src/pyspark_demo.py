import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType, IntegerType
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
from pyspark.ml.feature import IndexToString, VectorIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.regression import RandomForestRegressor

if __name__ == "__main__":
    conf = SparkConf().setAll([
        ("spark.sql.execution.arrow.enabled", "true"),
        ("spark.network.timeout", 100000000),
        ("spark.executor.heartbeatInterval", 10000000)
    ])

    sc = SparkContext(conf=conf)
    spark = SQLContext(sc)

    # Import data from S3 (PySpark)
    flights = spark.read.csv(
        "s3a://uptrend-pyspark-training/data/DelayedFlights.csv", header=True)

    # Show how many rows are in the CSV file
    print("Total Rows")
    flights.count()

    # Subset to 1000 rows for testing
    flights = flights.limit(1000)


    # Create a subset of the flights data
    print("Subsetting Data")
    flights_sub = flights.select("DayOfMonth", "Distance")

    # Convert columns from integers to strings

    flights_sub = flights_sub.withColumn("DayofMonth", flights_sub["DayofMonth"].cast(IntegerType()))
    flights_sub = flights_sub.withColumn("Distance", flights_sub["Distance"].cast(IntegerType()))

    labelIndexer = StringIndexer(
        inputCol="Distance", outputCol="indexedDistance").fit(flights_sub)

    model_features = ["DayofMonth"]

    vec_assembler = VectorAssembler(inputCols = model_features, outputCol = "features")


    # Split data for training model (80/20 split)
    (train, test) = flights_sub.randomSplit([0.8, 0.2])


    # Create Random Forest Classifier
    rf = RandomForestClassifier(numTrees=3, maxDepth=2, labelCol="Distance", seed=42)
    rf.fit(flights_sub)
