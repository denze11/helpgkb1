#!/bin/bash
source '/home/helpgkb1/sites/helpgkb1/main/env/bin/activate'
exec gunicorn -c '/home/helpgkb1/sites/helpgkb1/main/gunicorn_config.py' main.wsgi
