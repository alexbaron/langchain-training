#!/bin/bash

source .venv/bin/activate

cd 01-llm-chat

uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8000