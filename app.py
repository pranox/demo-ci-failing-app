from flask import Flask

# Intentional error for CI demo
import not_a_real_module  # ❌ this will fail

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, broken app!"

if __name__ == "__main__":
    app.run()
