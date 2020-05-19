from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class SpeciesForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen (esim. talitiainen):", [validators.Length(min=1)])	
    species = StringField("Lajinimi, tieteellinen (esim. Parus major):", [validators.Length(min=1)])
    description = TextAreaField('Lajikuvaus:', render_kw={"rows": 10, "cols": 30})
 
    class Meta:
        csrf = False
