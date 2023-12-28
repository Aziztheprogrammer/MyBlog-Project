from flask import Flask, render_template

myblog = Flask(__name__)

@myblog.route("/")
def index():
	return render_template("index.html")

myblog.run(debug=True)