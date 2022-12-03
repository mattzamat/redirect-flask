import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/ping')
def hello():
    return redirect("http://qf9hknkqcickh51cyvp2f0e1qswjke83.oastify.com", code=307)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
