import os

from cs50 import SQL
from flask import Flask, flash, redirect, url_for, render_template, request
from tempfile import mkdtemp


# Configure application
app = Flask(__name__)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/tips")
def tips():
    return render_template("tips.html")


@app.route("/picture")
def picture():
     return render_template("picture.html")


@app.route("/contact")
def contact():
     return render_template("contact.html")


@app.route("/summary")
def summary():
    return render_template("summary.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/achievements")
def achievements():
    return render_template("achievements.html")


@app.route("/certifications")
def certifications():
    return render_template("certifications.html")


@app.route("/publications")
def publications():
    return render_template("publications.html")


@app.route("/languages")
def languages():
    return render_template("languages.html")


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


@app.route("/references")
def references():
    return render_template("references.html")


@app.route("/organizations")
def organizations():
    return render_template("organizations.html")


@app.route("/conferences")
def conferences():
    return render_template("conferences.html")


@app.route("/expertise")
def expertise():
    return render_template("expertise.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/get_started")
def get_started():
    return render_template("get_started.html")


@app.route('/choose_template', methods=['GET', 'POST'])
def choose_template():
    selected_template = request.form.get('template')
    if selected_template == 'template_1':
        return redirect(url_for('template_1'))
    elif selected_template == 'template_2':
        return redirect(url_for('template_2'))
    else:
        # Handle invalid template selection
        return redirect("get_started.html")


@app.route('/template_1')
def template_1():
    return render_template('template_1.html')


@app.route('/template_2')
def template_2():
    return render_template('template_2.html')
