from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

last_update = datetime.utcnow().strftime("%a, %d %b %Y, %H:%M:%S")

@app.route('/', methods=['GET'])
def index():
    con = sqlite3.connect('onions.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    getonions = db.execute('select name, address, status, status_nb from Onions')
    return render_template('index.html', last_update=last_update, onions=getonions.fetchall())



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')