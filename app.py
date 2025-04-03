from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    print(np.sqrt(25))
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)