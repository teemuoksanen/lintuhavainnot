from application import app, db
from flask import redirect, render_template, request, url_for
from application.species.models import Species
from application.species.forms import SpeciesCreationForm, SpeciesEditForm



@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new/")
def species_form():
    return render_template("species/new.html", form = SpeciesCreationForm())

@app.route("/species/edit/<species_id>/", methods=["GET", "POST"])
def species_edit_information(species_id):

    species = Species.query.get(species_id)
    
    if request.method == "POST":

        form = SpeciesEditForm(request.form) 

        if not form.validate():
            return render_template("species/edit.html", species=species, form = form)

        species.name = form.name.data
        species.species = form.species.data
        species.description = form.description.data

        db.session().commit()
  
        return redirect(url_for("species_index"))

    return render_template("species/edit.html", species=species, form = SpeciesEditForm(obj=species))

@app.route("/species/delete/<species_id>/", methods=["POST"])
def species_delete(species_id):

     species = Species.query.get(species_id)
     db.session.delete(species)
     db.session.commit()
     return redirect(url_for("species_index"))

@app.route("/species/", methods=["POST"])
def species_create():

    form = SpeciesCreationForm(request.form) 

    if not form.validate():
        return render_template("species/new.html", form = form)

    species = Species(form.name.data, form.species.data, form.description.data)

    db.session().add(species)
    db.session().commit()
  
    return redirect(url_for("species_index"))

