from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, MultipleFileField, validators
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.widgets import TextArea


class ItemForm(FlaskForm):
    images = MultipleFileField(u'Image File', validators=[DataRequired()])

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
    brand = StringField('Brand', validators=[DataRequired(), Length(min=1, max=20)])
    short_Description = StringField('Short Description', validators=[DataRequired(), Length(min=1, max=20)])
    description = StringField('Description', validators=[DataRequired(), Length(min=1, max=50)], widget=TextArea())
    mrp = IntegerField('M R P', validators=[DataRequired()])
    discount = IntegerField('Discount', validators=[DataRequired()])
    productDetails = StringField('Product Details', validators=[DataRequired(), Length(min=1, max=50)], widget=TextArea())
    material_Care = StringField('Material & Care', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Submit')
