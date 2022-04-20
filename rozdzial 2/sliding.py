from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.types import (
StructType,
StructField,
StringType,
IntegerType,
TimestampType,
)

server = "localhost:9092"
spark = SparkSession.builder\
        .appName("tumb")\
        .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
raw = (spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "127.0.0.1:9092")\
    .option("subscribe", "okna")\
    .load()
)

json_schema = StructType(
    [
        StructField("time", TimestampType()),
        StructField("id", StringType()),
        StructField("value", IntegerType()),
    ]
)
parsed = raw.select(
    "timestamp", f.from_json(raw.value.cast("string"),
                 json_schema).alias("json")
    ).select(
    f.col("json").getField("time").alias("event_time"),
    f.col("json").getField("id").alias("id"),
    f.col("json").getField("value").alias("value"),
    )
group = parsed.where("id != 'a' and id != 'b'")\
          .groupBy(f.window("proc_time", "20 seconds",
                            "10 seconds"), "id")\
          .count()
query = (
    group.writeStream.outputMode("complete")\
    .format("console")\
    .option("truncate", "false")\
    .start()
)
query.awaitTermination(600)
query.stop()