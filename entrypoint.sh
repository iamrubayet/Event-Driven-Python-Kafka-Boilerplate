#!/bin/bash

# Run each Python script
python3 transaction.py &
python3 email.py &
python3 analytics.py &
python3 order_backend.py &

# Wait for all background processes to finish
wait
