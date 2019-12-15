# myproject/owners/views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.owners.forms import AddForm
from myproject.models import Owner

owners_blueprint = Blueprint(
    'owners', __name__, template_folder='templates/owners'
)


@owners_blueprint.route('/add', methods=['GET', 'POST'])
def addo():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.puppy_id.data

        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.lists'))

    return render_template('addo.html', form=form)
