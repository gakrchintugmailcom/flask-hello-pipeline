from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Login Page</h1>
    <form>
        <input placeholder='Username'><br>
        <input type='password' placeholder='Password'><br>
        <button>Login</button>
    </form>
    """

if __name__ == '__main__':
    app.run()

