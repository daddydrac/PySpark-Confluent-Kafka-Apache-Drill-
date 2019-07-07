#!/usr/bin/env bash

# Bind Anaconda to Spark
echo -e "\nexport PYSPARK_PYTHON=/home/hadoop/conda/bin/python" >> /etc/spark/conf/spark-env.sh
# echo "export PYSPARK_DRIVER_PYTHON=/home/hadoop/conda/bin/jupyter" >> /etc/spark/conf/spark-env.sh
# echo "export PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --ip=$1'" >> /etc/spark/conf/spark-env.sh
echo "export MASTER='yarn'" >> /etc/spark/conf/spark-env.sh

sh /etc/spark/conf/spark-env.sh