import redis
from kafka import KafkaProducer, KafkaConsumer

from config.kafka_settings import kafka_settings
from config.redis_settings import redis_settings


class KafkaService:
    def __init__(self):
        self.bootstrap_servers = kafka_settings.bootstrap_servers
        self.redis_client = redis.Redis(host=redis_settings.host, port=redis_settings.port)

    def send_message(self, topic, message):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        producer.send(topic, message)
        producer.close()

    def consume_messages(self, topic, group_id):
        consumer = KafkaConsumer(
            topic,
            group_id=group_id,
            bootstrap_servers=self.bootstrap_servers,
        )
        for message in consumer:
            print(f"Received message: {message.value}")
        consumer.close()

    def set_cache(self, key, value):
        self.redis_client.set(key, value)

    def get_cache(self, key):
        return self.redis_client.get(key)
