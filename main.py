
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/mvp')
def mvp():
    return render_template('mvp_design.html')

@app.route('/personas')
def personas():
    return render_template('user_personas.html')

@app.route('/challenges')
def challenges():
    return render_template('challenges.html')

if __name__ == '__main__':
    app.run(debug=True)
