from flask_wtf import FlaskForm
from wtfforms import StringField, SubmitField, FloatField
from wtfforms.validators import DataRequired


class ItemForm(FlaskForm):
	brand = StringField('Brand Name')
	name = StringField('Name',validators=[DataRequired()])
	mrp = FloatField('MRP', validators=[DataRequired()])
	discount = 