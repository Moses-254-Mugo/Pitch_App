from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms import validators
from wtforms.fields.core import SelectField
from wtforms.validators import Required
from ..models import User

class ReviewForm(FlaskForm):

    title = StringField('Give your title',validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    text = TextAreaField('Text', validators=[Required()])
    title = StringField('Text', validators= [Required()])
    category = SelectField('Type',choices=[('investor','Pitch for Investors'),('employee','Pitch for Employees'),('customer','Pitch for Customers')],validators=[Required()])
    submit = SubmitField('Submit')