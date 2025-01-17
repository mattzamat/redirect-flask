import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return redirect("https://vsrdwxqyeat2rx42v3v9b8tqghm8a0yp.oastify.com", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
