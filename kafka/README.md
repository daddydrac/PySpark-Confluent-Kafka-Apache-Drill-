# Kafka

This folder contains the lesson for Apache Kafka

## Dataset

* Examples used from the tutorial.

## Tutorial - Kafka Quickstart

1. Download Kafka to your computer. Run the following commands.

    `tar -xzf kafka_2.11-2.0.0.tgz`

    `cd kafka_2.11-2.0.0`

2. To start the server, you need to start Zookeeper, which is indide the Kafka folder you downloaded.

    `bin/zookeeper-server-start.sh config/zookeeper.properties`

3. Start the Kafka server.

    `bin/kafka-server-start.sh config/server.properties`

4. Create a test topic. This will have a single partition, and one replica.

    `bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test`

    You should see the `test` topic with the following command.

    `bin/kafka-topics.sh --list --zookeeper localhost:2181`

5. To send messages, keep your current terminal open, then open a new terminal window. In the new window, run the following, then type some message text to send to the `test` topic.

    `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test`

6. To receive messages, opan another new terminal window. Then, start a consumer with the following command.

    `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning`

    As you type messages into the producer terminal created in step 5, you'll see the text appear in the consumer terminal.


## Resources
