# myproject/puppies/views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from .forms import AddForm, DelForm
from myproject.models import Puppy


puppies_blueprint = Blueprint(
    'puppies', __name__, template_folder='templates/puppies'
)


@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html', form=form)


@puppies_blueprint.route('del', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        pup_id = form.id.data

        pup = Puppy.query.get(pup_id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list.puppies'))

    return render_template('delete.html', form=form)
