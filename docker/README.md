# Docker - Pyspark/Kafka & Apache Drill

This folder contains files for building images for PySpark/ Kafka and Apache Drill.

## Requirements

* Docker - Spark/Kafka/Cassandra  | `yannael/kafka-sparkstreaming-cassandra`
* Docker - Drill  | `harisekhon/apache-drill`
* PyDrill | `pip instal pydrill`

## Lesson - Combining All Containers/ Services

1. Download the Spark/Kafka/Cassandra container.
    ```docker
    docker pull yannael/kafka-sparkstreaming-cassandra
    ```
2. Run the container with the following command.
    ```docker
    docker run -v `pwd`:/home/guest/uptrend -p 4040:4040 -p 8888:8888 -p 23:22 -ti --privileged yannael/kafka-sparkstreaming-cassandra

    ```

3. Within the container terminal, use the bash command to start all services.
    ```bash
    bash /usr/bin/startup_script.sh
    ```

4. After seeing Cassandra's status is `OK`, change the user to guest with the command below.
    ```bash
    su guest
    ```

5. Start a Jupyter notebook instance within the container.
    ```bash
    notebook
    ```

6. In your web browser, type `localhost:8888` into the URL bar. You'll be taken to the Jupyter notebooks.

    * Once you're in the notebook directory, click the `notebooks` folder.

7. Launch the `kafkaSendDataPy.ipynb` notebook. Run each of the cells.

8. After completing step 7, launch the `kafkaReceiveAndSaveToCassandraPy.ipynb` notebook.

9. After completing the `kafkaReceiveAndSaveToCassandraPy.ipynb` notebook, launch the Drill container with the following command.
    ```bash
    docker run -i --name pydrill -v `pwd`:/drill -p 8047:8047 -t harisekhon/apache-drill
    ```

10. Open the `Uptrend - PySpark With Docker` notebook for the tutorial.

## References

* [Docker For Data Science](https://towardsdatascience.com/docker-for-data-science-9c0ce73e8263)
* [Stack Overflow - Multi Stage Builds](https://stackoverflow.com/questions/39626579/is-there-a-way-to-combine-docker-images-into-1-container)
* [Docker Networking - Connect Multiple Containers](https://scotch.io/@Mozartted/docker-networking-how-to-connect-multiple-containers#toc-connecting-containers)
* [Connecting Two Docker Containers](https://stackoverflow.com/questions/45481943/connecting-two-docker-containers)
* [Docker - Published Ports](https://docs.docker.com/config/containers/container-networking/#published-ports)

* [Drill vs Spark](https://www.smartdatacollective.com/apache-drill-vs-apache-spark-what-s-right-tool-job/)

* [Python - Connect to Confluent Kafka Issues](https://github.com/confluentinc/confluent-kafka-python/issues/447)

* [Spark vs. Hadoop vs. Drill](https://www.quora.com/Which-is-more-efficient-Spark-over-Hadoop-or-Apache-Drill)