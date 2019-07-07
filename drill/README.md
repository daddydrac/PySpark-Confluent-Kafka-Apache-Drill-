# Apache Drill

This folder contains the lesson for Apache Drill.

## Lesson - Intro To Apache Drill

Download the Apache Drill Docker container.

```docker
docker pull drill/apache-drill:1.14.0
```

After downloading, run the Drill container. In order to mount a volume using `-v`, you must specify the full directory. For example, on my local computer, my full directory to the `drill` folder is the following:

```markdown
/home/greg/Spark-Kafka-Drill-Docker/drill
```

```docker
docker run -i --name drill-1.14.0 -v /full/directory/path/:/drill -p 8047:8047 -t drill/apache-drill:1.14.0
```

In another terminal window, run `jupyter notebook`. You should now be able to run the `PyDrill Tutorial - Intro to Apache Drill` notebook.

## Lesson - Querying The Yelp Dataset

The [Yelp dataset](https://www.yelp.com/dataset/challenge) is a great way to gain exposure to Drill. Download and unzip the dataset, then move all JSON files to the `data` folder.

If you've alreaady run the Docker command above, you'll be able to run the `Apache Drill - Querying The Yelp Dataset` notebook.

## References

[Drill Introduction](https://drill.apache.org/docs/drill-introduction/)

[Drill Tutorials](https://drill.apache.org/docs/tutorials-introduction/)