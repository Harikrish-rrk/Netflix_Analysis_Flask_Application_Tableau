from flask import Flask,render_template

from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/workbook')
def tableau():
    return render_template('workbook.html')
@app.route('/stories')
def stories():
    return render_template('stories.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/contributors')
def contributors():
    return render_template('contributors.html')
@app.route('/software')
def software():
    return render_template('software.html')    

