from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField

class AddSnackForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    is_healthy = BooleanField("This is a Healthy Snack")
    
    # category = RadioField("Category", choices= [('ic', 'Ice cream'), ('chips', 'Potato chips'), ('candy', 'Candy / Sweets')])
    category = SelectField("Category", choices= [('ic', 'Ice cream'), ('chips', 'Potato chips'), ('candy', 'Candy / Sweets')])
    
    
class NewEmployeeForm(FlaskForm):
    
    name = StringField("Employee Name")
    state = StringField("State Name")
    dept_code = SelectField("Department Code")