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

# Another method to delete.............
# @app.route('/delete/<int:id>')
# def delete_ninja(id):
#     ninja.Ninja.delete_one(id)
#     return redirect(request.referrer)
    

# @app.route('/delete/<int:id>')
# def delete_ninja(id):
#     data = {
#         'id':id
#     }
#     one_ninja = ninja.Ninja.get_one_ninja(data)
#     ninja.Ninja.delete_one(one_ninja.id)
#     return redirect(f"/onedojo/{one_ninja.dojo_id}")

@app.route('/delete/<int:id>/<int:dojo_id>')
def delete_ninja(id,dojo_id):
    ninja.Ninja.delete_one(id)
    return redirect(f"/onedojo/{dojo_id}")


@app.route('/edit/ninja/<int:id>')
def edit_ninja_details(id):
    data = {
        'id':id
    }
    return render_template("edit_ninja.html", one_ninja = ninja.Ninja.get_one_ninja(data))

@app.route('/update/ninja', methods = ["POST"])
def edit_ninja():
    ninja.Ninja.update_ninja(request.form)
    return redirect(f"/onedojo/{request.form['dojo_id']}")

