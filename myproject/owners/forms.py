# FORMS.PY owners
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of the Owner:')
    puppy_id = IntegerField('Id Number of Puppy:')
    submit = SubmitField('Add Owner')
