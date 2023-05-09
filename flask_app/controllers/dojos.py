from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja



@app.route('/dojos')
def dojo_dashboard():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("dojo_dashboard.html", all_dojos = dojos)


@app.route('/dojo/create', methods = ["POST"])
def create_dojo():
    data = {
        'name':request.form['name']
    }
    dojo.Dojo.save_dojo(data)
    return redirect('/dojos')


@app.route('/onedojo/<int:id>')
def show_one_dojo(id):
    data = {
        'id':id
    }
    return render_template("show_dojo.html", one_dojo = dojo.Dojo.get_dojo_with_ninjas(data)) 



