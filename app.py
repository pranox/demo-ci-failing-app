from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    x = 10
    y = 0
    return str(x / y)  # 🚨 ZeroDivisionError

if __name__ == "__main__":
    app.run()
