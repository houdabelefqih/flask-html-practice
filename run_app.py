import os
from flask import Flask, request, redirect, url_for, abort, render_template


app = Flask(__name__)


@app.route('/index')
def index():
    user = request.args.get('user', 'Guido Van Rossum')
    html = """
        <html>
            <h1>Hello {}!</h1>
        </html>
    """.format(user.title())
    return html


@app.route('/get-form', methods=['GET'])
def get_login_form():
    html = """
        <form action="/post-form" method="POST">
            <div>
                <label>Username</label>
                <input name="username">
            </div>
            <div>
                <label>Password</label>
                <input name="password" type="password">
            </div>
            <button type="submit">Submit</button>
        </form>
    """
    return html


@app.route('/post-form', methods=['POST'])
def post_login_form():
    user = request.form['username']
    return redirect(url_for('index', user=user))


@app.route('/login-form', methods=['GET', 'POST'])
def login_form():
    html = """
            <form action="/post-form" method="POST">
                <div>
                    <label>Username</label>
                    <input name="username">
                </div>
                <div>
                    <label>Password</label>
                    <input name="password" type="password">
                </div>
                <button type="submit">Submit</button>
            </form>
        """
    if request.method == 'GET':
        return html

    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            return redirect(url_for('index', user=username))
        else:
            abort(404)
    else:
        pass


# Extra task
# NOTE: Use '/profile' URL for this view
@app.route('/profile', methods=['GET'])
def profile():

    USER_DATA = {
        'first_name': 'Guido',
        'last_name': 'van Rossum',
        'age': 62,
        'birthdate': '31 January 1956',
        'nationality': 'Dutch',
        'worked_at': [
            'Python language development',
            'Google',
            'Dropbox'
        ]
    }
    return render_template('profile.html', user_data=USER_DATA)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
