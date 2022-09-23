from flask import *

app = Flask(__name__)

@app.route('/secret_route')
def secret():
    password = request.args.get('secret_key')
    if password == '[REDACTED]':
        return "Your secret is [REDACTED]"
    else:
        return "booo you can't find my secret dum dum"

@app.route('/')
def hello_world():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run('127.0.0.1', 5000)