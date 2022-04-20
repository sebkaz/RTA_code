import json
import random
from datetime import datetime, timedelta
from time import sleep

from kafka import KafkaProducer

if __name__=="__main__":
# lokalny serwer kafki
    server = "localhost:9092"
    producer = KafkaProducer(
        bootstrap_servers=[server],
        value_serializer=lambda x: json.dumps(x)
        .encode("utf-8"),
        api_version=(3,1,0),
    )
    try:
        while True:
            message = {
            "time": str(datetime.now() + \
            timedelta(seconds=random.randint(-15,0))
            ),
            "id" : random.choice(["a","b","c","d"]),
            "value":random.randint(0,100),
            }
            producer.send("okna", value=message)
            sleep(1)
    except KeyboardInterrupt:
        producer.close()