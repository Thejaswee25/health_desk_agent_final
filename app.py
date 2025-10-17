from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes.chatbot_routes import chatbot_bp
from routes.dashboard_routes import dashboard_bp
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('database','healthdesk.db')
app.config['SECRET_KEY'] = 'replace-with-secure-key'
db = SQLAlchemy(app)

app.register_blueprint(chatbot_bp, url_prefix='/api')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
