from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class AddSnackForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Snack Name", validators=[InputRequired()])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    is_healthy = BooleanField("This is a Healthy Snack")
    
    # category = RadioField("Category", choices= [('ic', 'Ice cream'), ('chips', 'Potato chips'), ('candy', 'Candy / Sweets')])
    category = SelectField("Category", choices= [('ic', 'Ice cream'), ('chips', 'Potato chips'), ('candy', 'Candy / Sweets')])
    
    
class NewEmployeeForm(FlaskForm):
    
    name = StringField("Employee Name")
    state = SelectField("State Name", choices=[(st,st) for st in states])
    dept_code = SelectField("Department Code")