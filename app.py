import sqlite3 as sq
from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    try:
        conn = sq.connect('data.db')
        c = conn.cursor()
        c.execute(""" 
        CREATE TABLE products_list (
            prod TEXT,
            quant INT
        );
        """)
    except:
        print('[DATA BASE OK]')

    return '<h1>OK</h1>'


@app.route('/add')
def inset():
    return render_template('colect.html')

class show_off(Resource):
    def get(self):
        conn_2 = sq.connect('data.db')
        cr = conn_2.cursor()
        cr.execute(""" 
        SELECT * FROM products_list
        """)

        for i in cr.fetchall():
            for i in cr.fetchall():
                return f'[ {i} : {j} ]'

api.add_resource(show_off, '/view')

if __name__ == "__main__":
    app.run()