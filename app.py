from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hello():
    return "Time is: " + time.asctime(time.localtime(time.time()))


if __name__ == '__main__':
    app.run()
