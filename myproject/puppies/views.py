# myproject/puppies/views.py
from flask import Blueprint, render_template, redirect, url_for, flash
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy


puppies_blueprint = Blueprint(
    'puppies', __name__, template_folder='templates/puppies'
)


@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def addp():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.lists'))

    return render_template('addp.html', form=form)


@puppies_blueprint.route('/list')
def lists():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        pup_id = form.id.data

        pup = Puppy.query.get(pup_id)
        flash(f'{pup.name} has been adopted, so it\'s no longer in our database')

        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.delete'))

    return render_template('delete.html', form=form)
