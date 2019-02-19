from flask_wtf import FlaskForm
import itertools
from wtforms import StringField, SubmitField, IntegerField, FileField, DateField,MultipleFileField, validators, Field
from wtforms.validators import DataRequired, Length, ValidationError,Email
from wtforms.widgets import TextArea, TextInput
from flask_wtf.file import FileField, FileAllowed, FileRequired


class SellerForm(FlaskForm):
    first_name= StringField('First Name', validators=[DataRequired(), Length(min=2, max=15)])
    last_name=StringField('Last Name', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    date_of_birth=DateField('Date Of Birth', validators=[DataRequired()])
    picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
    
    address=StringField('Permanent Address', validators=[DataRequired()])
    state=StringField('State',validators=[DataRequired()])
    pin_code=IntegerField('PIN CODE',validators=[DataRequired()])
    gstin=IntegerField('GST Number', validators=[DataRequired()])
   
    adhar_card_no=IntegerField('Adhar Card Number',validators=DataRequired())

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
    submit = SubmitField('Submit')


class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]

        else:
            self.data = []


class SizeQtyField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            d = [x.strip() for x in valuelist[0].split(',')]
            m = dict(itertools.zip_longest(*[iter(d)] * 2, fillvalue=""))
            for key in m:
                if(type(m[key]) != type(1)):
                    m[key] = int(m[key])
            self.data = m

        else:
            self.data = {'S': 0}


class ItemForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    typeofitem = StringField('Type', validators=[DataRequired(), Length(min=2, max=20)])
    images = MultipleFileField(u'Image File', validators=[DataRequired()])

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
    brand = StringField('Brand', validators=[DataRequired(), Length(min=1, max=20)])
    short_Description = StringField('Short Description', validators=[DataRequired(), Length(min=1, max=50)])
    description = StringField('Description', validators=[DataRequired(), Length(min=1, max=200)])
    mrp = IntegerField('M R P', validators=[DataRequired()])
    discount = IntegerField('Discount', validators=[DataRequired()])
    sizenqty = SizeQtyField('Size and Quantity ', validators=[DataRequired()])
    productDetails = TagListField('Product Details', validators=[DataRequired()])
    material_Care = TagListField('Material & Care', validators=[DataRequired()])
    tags = TagListField('Tags', validators=[DataRequired()])
    submit = SubmitField('Submit')
