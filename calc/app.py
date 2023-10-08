from flask import Flask, request
from operations import add,sub,mult,div
app = Flask(__name__)


@app.route('/add')
def add_nums():
    a = request.args.get('a')
    b = request.args.get('b')
    a=int(a)
    b=int(b)
    sum= add(a,b)
    return str(sum)


@app.route('/sub')
def subtract_nums():
    a = request.args.get('a')
    b = request.args.get('b')
    a=int(a)
    b=int(b)
    diff= sub(a,b)
    return str(diff)


@app.route('/mult')
def multiply_nums():
    a = request.args.get('a')
    b = request.args.get('b')
    a=int(a)
    b=int(b)
    prod=mult(a,b)
    return str(prod)

@app.route('/div')
def divide_nums():
    a = request.args.get('a')
    b = request.args.get('b')
    a=int(a)
    b=int(b)
    divide=div(a,b)
    return str(divide)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)