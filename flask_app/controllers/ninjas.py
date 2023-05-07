from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo,ninja

# for testing app functionality
@app.route('/')
def index():
    return "sucess"

@app.route('/ninja/create',  methods = ["POST"])
def create_ninja():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojos_id']
    }
    ninja.Ninja.save_ninja(data)
    return redirect(f"/onedojo/{request.form['dojos_id']}")

@app.route('/new/ninja')
def new_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("new_ninja.html", all_dojos = dojos)