from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hello():
    return "Time is: " + time.asctime(time.localtime(time.time()))


@app.route('/author')
def author():
    return "Author's name is Artsemi Dzmitryieu."


if __name__ == '__main__':
    app.run()
