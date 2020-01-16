from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


genre_choices = [
    (0, 'Please select ...'),
    (1, 'Carnatic Traditional'),
    (2, 'Carnatic Modern'),
    (3, 'English Old'),
    (4, 'English'),
    (5, 'Kannada Old'),
    (6, 'Kannada'),
    (7, 'Tamil Old'),
    (8, 'Tamil'),
    (9, 'Hindi Old'),
    (10, 'Hindi')
]


class YTDownloadForm(FlaskForm):
    ytlink = StringField('YouTube Link',
                         validators=[DataRequired()])
    artists = StringField('Artist(s)',
                          validators=[DataRequired()])
    album = StringField('Album',
                        validators=[DataRequired()])
    album_artist = StringField('Album Artist',
                               validators=[DataRequired()])
    genre = SelectField('Genre', coerce=int, choices=genre_choices,
                        validators=[DataRequired()])
    download = SubmitField('Download MP3')
