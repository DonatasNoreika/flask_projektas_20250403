from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    print(np.sqrt(25))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)