from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the index page'

@app.route('/home')
def home():
    return '<marquee>this is something</marquee>'

@app.route('/home/<username>')
def user_home(username):
    return 'Hello, {}'.format(username)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('home'))
#     print(url_for('user_home', username='ahyan'))
#     print(url_for('user_home_with_password', username='ahyan', password='passissomething'))


@app.route('/home/<username>/<password>')
def user_home_with_password(username, password):
    return 'Hello, {}! Your password is {}'.format(username, password)

if __name__ == '__main__':
    app.run(port=3020, debug=True)
