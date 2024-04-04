from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'API para Teste Exati'

if __name__ == '__main__':
    app.run(debug=True)