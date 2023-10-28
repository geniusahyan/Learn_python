from flask import Flask, request, render_template , redirect , make_response

import datetime

app = Flask(__name__)

@app.route('/home', methods=['post'])
def home():
    now = datetime.datetime.now()
    return render_template('home.html', cur_now=now)

@app.route('/about')
def about():
    headers = {
        'Content-Type': 'application/json'
    }
    return make_response('this is response gen', 200, headers)

@app.route('/base')
def base():
    return redirect('/home')


@app.route('/search')
def search():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(port=3020, debug=True)
