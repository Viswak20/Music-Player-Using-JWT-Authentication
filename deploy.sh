cd /home/ubuntu/Music-Player-Using-JWT-Authentication

echo "Pull latest code"
git pull origin main

echo "Activate virtual env"
source venv/bin/activate

echo "Stop old server"
pkill -f runserver || true

echo "Start server"
nohup python3 manage.py runserver 0.0.0.0:8000 &