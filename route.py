from flask import Flask, render_template
from flask_cors import CORS
from manager import manager_bp

app = Flask(__name__)
CORS(app)

# 注册 manager_bp Blueprint
app.register_blueprint(manager_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2023)
