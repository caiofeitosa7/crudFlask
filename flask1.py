from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

# db = MySQL(app)

# from views import *


@app.route('/')
def index():
    return 'Hello World'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
