from flask import Flask, request, redirect, jsonify, render_template


app = Flask(__name__) 

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/book-us-now', methods=['POST','GET'])
def book():
    return render_template('order.html')

@app.route('/request-a-quote', methods=['POST','GET'])
def quote():
    return render_template('quote.html')


if __name__ == "__main__":
    app.run(debug=True)
