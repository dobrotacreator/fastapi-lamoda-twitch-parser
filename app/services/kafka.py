import importlib
import logging

import aioredis
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from config import settings


class KafkaService:
    def __init__(self):
        self.bootstrap_servers = settings.kafka_settings.bootstrap_servers
        self.redis_host = settings.redis_settings.host
        self.redis_port = settings.redis_settings.port
        self.logger = logging.getLogger("KafkaService")  # Create a logger instance

    async def send_message(self, topic, message: str):
        producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await producer.start()
        try:
            self.logger.info(f"Sending message: {message}")
            record_metadata = await producer.send(topic, message.encode('utf-8'))
            result = await record_metadata
            self.logger.info("Message sent successfully")
            self.logger.info(f"Record metadata: {result}")
        except Exception as e:
            self.logger.error(f"Error sending message: {e}")
        finally:
            await producer.stop()

    async def process_message(self, message):
        try:
            # The message contains the module name, the function and the task separated by a @
            module_name, function_name, task = message.decode('utf-8').split('@')
            module = importlib.import_module(module_name)
            function = getattr(module, function_name)
            await function(task)
        except Exception as e:
            self.logger.error(f"Error processing message: {e}")

    async def consume_messages(self, topic, group_id):
        consumer = AIOKafkaConsumer(
            topic,
            group_id=group_id,
            bootstrap_servers=self.bootstrap_servers,
        )
        self.logger.info("Working...")
        try:
            await consumer.start()
            async for message in consumer:
                self.logger.info(f"Received message: {message.value}")
                await self.process_message(message.value)
        finally:
            await consumer.stop()

    async def set_cache(self, key, value):
        redis = await aioredis.from_url('redis://redis')
        await redis.set(key, value)
        redis.close()
        await redis.wait_closed()

    async def get_cache(self, key):
        redis = await aioredis.from_url('redis://redis')
        result = await redis.get(key)
        redis.close()
        await redis.wait_closed()
        return result
