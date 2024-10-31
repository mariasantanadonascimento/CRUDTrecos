app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p> Olá Mundo!</p>"