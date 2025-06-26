#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r idproof/requirements.txt

cd idproof
python manage.py collectstatic --no-input
python manage.py migrate
