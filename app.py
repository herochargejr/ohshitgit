from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
# maybe i should add a feature which only I can see
# it'll be soo fun
if __name__ == '__main__':
    app.run('127.0.0.1', 5000)