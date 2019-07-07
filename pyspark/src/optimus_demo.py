from optimus import Optimus


if __name__ == "__main__":

    # Import data from S3 (Optimus)
    op = Optimus()
    flights = op.load.csv("s3a://uptrend-pyspark-training/data/DelayedFlights.csv", header=True)

    # Show how many rows are in the CSV file
    flights.count()

    # Review the schema and variables of Spark DataFrame
    flights.printSchema()

    # Create subset of the data
    flights_sub = flights.limit(5000)

    # Subset based on columns
    flights_sub = flights.select("Distance", "Dest")

    # Review the schema of the DataFrame
    flights_sub.printSchema()


    # Create Random Forest classifier

    rf_predict, rf_model = op.ml.random_forest(flights_sub, flights_sub.columns, "Dest")



