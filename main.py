import psycopg2
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

app.config.from_pyfile('config.py')

try:
    con = psycopg2.connect(app.config['DB_URL'])
    print('Connected to PostgreSQL successfully!')
except Exception as e:
    print(f'Connection Error: {e}')
    con = None

from user_view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5432, debug=True)
