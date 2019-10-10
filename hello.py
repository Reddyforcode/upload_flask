from flask import Flask, render_template, request
import os
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/', methods= ["GET", "POST"])
def hello():
    if(request.method=="POST"):
        file = request.files["file"]
        file.save(os.path.join("uploads", file.filename ))
        """renders a sample page"""
        return render_template("index.html", message="success")
    return render_template("index.html", "uploads")


if __name__=='__main__':
    """
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    """
    app.run(host='0.0.0.0')