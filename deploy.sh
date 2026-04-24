#!/bin/bash

cd /home/ubuntu/Music-Player-Using-JWT-Authentication

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install -r requirements.txt

pkill -f gunicorn || true

nohup gunicorn musicplayer.wsgi:application --bind 0.0.0.0:8000 > output.log 2>&1 &