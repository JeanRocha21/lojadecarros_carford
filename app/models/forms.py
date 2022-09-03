from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

CAR_CHOICES = [('Não possui','Não possui'),('Hatch','Hatch'), ('Sedan', 'Sedan'), ('Convertible', 'Convertible')]
COLORS_CHOICES = [('',''),('Yellow', 'Yellow'),('Blue', 'Blue'),('Gray', 'Gray')]

class Cadastro(FlaskForm):
    client = StringField("Cliente", validators=[DataRequired()])
    car1 = SelectField("Carro 1", choices=CAR_CHOICES)
    color1 = SelectField("Qual a cor do carro 1?", choices=COLORS_CHOICES)
    car2 = SelectField("Carro 2", choices=CAR_CHOICES)
    color2 = SelectField("Qual a cor do carro 2?", choices=COLORS_CHOICES)
    car3 = SelectField("Carro 3", choices=CAR_CHOICES)
    color3 = SelectField("Qual a cor do carro 3?", choices=COLORS_CHOICES)




