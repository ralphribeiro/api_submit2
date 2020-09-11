python -m unittest test/tests_api.py -v
flask db init
flask db migrate
flask run -h 0.0.0.0