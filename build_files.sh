PYTHON=${PYTHON:-python3}
$PYTHON -m pip install --break-system-packages -r requirements.txt
$PYTHON manage.py collectstatic --noinput --clear
$PYTHON manage.py migrate
