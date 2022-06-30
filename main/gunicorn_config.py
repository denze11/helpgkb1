command = '/home/helpgkb1/sites/helpgkb1/main/env/bin/gunicorn'
pythonpath = '/home/helpgkb1/sites/helpgkb1/'
bind = '127.0.0.1:8001'
workers = 5
user = 'helpgkb1'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=main.settings'
