#!/bin/bash

until mongo --quiet --eval "db.adminCommand('ping')" &>/dev/null; do
  echo "Waiting for MongoDB..."
  sleep 5
done

uvicorn main:app --host 0.0.0.0 --port 8000
