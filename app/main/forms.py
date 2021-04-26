from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from ..models import Pitch
from wtforms import ValidationError

        
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')        
            
            
class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Interview','Interview'),('Promotion','Promotion'),('Product','Product'),('Pickup','Pickup')],validators=[Required()])
    content = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Post')   
    
    def validate_pitch(self,data_field):
            if Pitch(title =data_field.data,content =data_field.data).first():
                raise ValidationError('Error in displaying pitch')


class CommentForm(FlaskForm):
    comment = TextAreaField('Pitch comment', validators=[Required()])
    submit = SubmitField('Submit')            