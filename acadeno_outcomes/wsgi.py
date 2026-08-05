import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acadeno_outcomes.settings')

application = get_wsgi_application()

if os.environ.get('VERCEL') and not os.path.exists('/tmp/db.sqlite3'):
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print("Migration error:", e)

app = application
