#!flask/bin/python
from flask import Flask
from flask import request
import sqlite3
import json

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def index():
    #print(request.data)
    try:
        data = json.loads(request.data)
        print(data)
        with sqlite3.connect("db.db") as con:
            con.execute("INSERT INTO light_log (`eui`,`r`,`g`,`b`,`ac`,`dc`,`motion`,`section`,`group`,`lum`,`softwareId`,`light`)\
            VALUES ('{0}',{1},{2},{3},{4},{5},{6},{7},'{8}',{9},'{10}',{11})".format(data["eui"],data["R"],data["G"],data["B"],data["AC"],data["DC"],data["Motion"],data["Section"],data["Group"],data["lum"],data["SoftwareId"],data["light"]));
            con.commit()
    finally:
        con.close()
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
