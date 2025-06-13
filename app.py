from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Ankit! This is your first Flask app."

@app.route('/about')
def about():
    return "This is the about page. You're learning Flask!"

if __name__ == '__main__':
    app.run(debug=True)

