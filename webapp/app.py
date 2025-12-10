
# lower case for module names, upper case for class names
from flask import Flask
# dunder names is associate the webapp with your code's current namesapace.
app = Flask(__name__)


@app.get('/')
def index():
    # when invoked, this function, called "index", returns this exciting string
    return "This is a placeholder for your webapp's opening page."

#This is the famous "dunder name equals dunder main" idiom. We've more to say about this "if" statement later.

if __name__ == '__main__':
    # This line of code runs Flask's built-in web server, then feeds your webapp code to it.
    app.run()
    