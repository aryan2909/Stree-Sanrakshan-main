from flask import Flask,render_template,Response



app=Flask(__name__)

@app.route("/")
def home():
     return render_template("index.html")

@app.route("/feed/")
def feed():
     return render_template("Feedback.html")

@app.route("/start/")
def start():
     return render_template("start.html")

@app.route("/start1/")
def start1():
     return render_template("start1.html")

@app.route("/start2/")
def start2():
     return render_template("start2.html")

@app.route("/start3/")
def start3():
     return render_template("start3.html")

@app.route("/vid1/")
def vid1():
     return Response()

@app.route("/vid2/")
def vid2():
     return Response()

@app.route("/vid3/")
def vid3():
     return Response()

@app.route("/vid4/")
def vid4():
     return Response()


if __name__=="__main__":
    app.run(host = "127.0.0.1",debug=True)