#!/usr/bin/env bash

python manage.py migrate

python manage.py loaddata graphQLapi/fixtures/cart.json
python manage.py runserver 0.0.0.0:8000