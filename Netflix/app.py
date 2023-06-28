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
@app.route('/tableau')
def tableau():
    return render_template('tableau.html')
@app.route('/contributors')
def contributors():
    return render_template('contributors.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/software')
def software():
    return render_template('software.html')    

