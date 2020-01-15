from flask import Flask, jsonify, request, render_template
import re
from bolsoxinga import functions

app = Flask(__name__)

@app.route('/')
def static_page():
    return render_template('index.html')

@app.route('/generate/<string:link>')
def Func_gerate(link):
    result = functions.set_xing(link)
    return render_template('index.html', result=[result])




if __name__ == '__main__':
    app.run(debug=True)