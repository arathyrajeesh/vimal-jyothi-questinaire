python -m pip install --break-system-packages -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migrate
