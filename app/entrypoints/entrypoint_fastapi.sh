#!/bin/bash

echo "Waiting for Kafka and MongoDB to be ready..."
sleep 15

python main.py
