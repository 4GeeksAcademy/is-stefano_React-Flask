  
import os
from flask_admin import Admin
from .models import db, Users, Followers, Comments, Medias, Posts, Characters, CharacterDetails, Planets, PlanetsDetails, Starships, StarshipsDetails
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Posts, db.session))
    admin.add_view(ModelView(Comments, db.session))
    admin.add_view(ModelView(Followers, db.session))
    admin.add_view(ModelView(Comments, db.session))
    admin.add_view(ModelView(Medias, db.session))
    admin.add_view(ModelView(Posts, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(CharacterDetails, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(PlanetsDetails, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(StarshipsDetails, db.session))
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))