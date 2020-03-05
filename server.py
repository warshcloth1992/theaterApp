from flask import Flask 
app = Flask(__name__)


@app.route('/')
def name():
	return "name"


if __name__ == "__main__":
	run.app('0.0.0.0', port=4000)
