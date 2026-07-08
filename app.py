from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Production Deployment using Jenkins CI/CD 🚀"

app.run(host="0.0.0.0", port=5000)
