# Import the flask library
from flask import Flask, request

# Create your web server
app = Flask(__name__)



# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    # Just a simple function that says Hello, World!
    return 'Hello hello!'

# You can message lol_bot via <your website>/lol
@app.route('/lol')
def lol_bot():
    # Get the value of the 'text' query parameter
    # request.args is a dictionary (cool!)
    text = request.args.get('text')
    # This bot lols at every command it gets sent!
    return f'lol {text}'


# Start the web server!

if __name__ == '__main__':
    # Start the web server!
    app.run()
