from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    x = 1/0
    return 'Index Page'
@app.route('/hello')
def hello():
    return 'Hello World'
if __name__ == '__main__':
    # Run the application at
    # the default port (5000)
    app.run(debug = True)