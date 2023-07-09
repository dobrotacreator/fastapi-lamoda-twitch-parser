#!/bin/bash

until mongo --quiet --eval "db.adminCommand('ping')" &>/dev/null; do
  echo "Waiting for MongoDB..."
  sleep 5
done

python main.py
