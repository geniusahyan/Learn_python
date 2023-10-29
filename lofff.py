from flask import Flask , render_template, make_response, request
import requests

app = Flask('__main__')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        res = make_response(render_template('base.html'))
        res.set_cookie('username',request.form.get('Name'))
        return res
    
    return render_template('data.html')


if __name__ == '__main__':
    app.run(debug=True)

