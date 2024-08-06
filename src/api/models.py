from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach}

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    firstname = db.Column(db.String(60), unique=True, nullable=False)
    laststname = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
         return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.laststname,
            "email": self.email }

    
class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author_to = db.relationship('Users', foreign_keys=[author_id])
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post_to = db.relationship('Posts', foreign_keys=[post_id], backref=db.backref('comment_to', lazy='select'))


class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('post_to', lazy='select'))


class Followers(db.Model):
    __tablename__ = "followers"
    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_from_to = db.relationship('Users', foreign_keys=[user_from_id])
    user_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to_to = db.relationship('Users', foreign_keys=[user_to_id])


class Medias(db.Model):
    __tablename__ = "medias"
    id = db.Column(db.Integer, primary_key=True)
    # media_type = db.Column(db.Enum('video', 'image', 'sounds', name="media_type") unique=True, nullable=False)
    comment_text = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    def __repr__(self):
            return f'<User {self.medias_type}'
    
    def serialize(self):
         return{
              'id': self.id,
              'media_type': self.media_type,
              'comment_text': self.comment_text,
              'author_id': self.author_id,
              'post_id': self.post_id
            } 

class Characters(db.Model):
    __tablename__= "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)


    def __repr__(self):
        return f'<Characters {self.name}>'

    def serialize(self):
        return {"uid": self.uid,
                "name": self.username}


class CharacterDetails(db.Model):
    __tablename__= "characters Details"
    firstname = db.Column(db.String(60), unique=True, nullable=False)
    laststname = db.Column(db.String(60), unique=True, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    gender = db.Column(db.String, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_to = db.relationship('Characters', foreign_keys=[character_id])

    def __repr__(self):
        return f'<Character {self.name} - {self.planet_origin}>'

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "firstname": self.firstname,
                "lastname": self.lastname}


class Starships(db.Model):
    __tablename__= "starship"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)

class StarshipsDetails(db.Model):
    __tablename__= "starships Details"
    model = db.Column(db.String(60), unique=True, nullable=False)
    type = db.Column(db.String(60), unique=True, nullable=False)
    length = db.Column(db.Integer)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_to = db.relationship('Starships', foreign_keys=[starship_id])
   
class Starships(db.Model):
    __tablename__= "starship"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)  

class Planets(db.Model):
    __tablename__= "starship"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)  

class PlanetsDetails(db.Model):
    __tablename__= "planets Details"
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(60), unique=True, nullable=False)
    climate = db.Column(db.String(60), unique=True, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_to = db.relationship('Planets', foreign_keys=[planet_id])

class Favoritos(db.Model):
    __tablename__= "Favoritos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('user_to', lazy='select'))
    
    def __repr__(self):
        return f'El item favorito de {self.user_id} es {self.item}'
    
    def serialize(self):
        return{"id": self.id,
               "item": self.item,
               "user_id": self.user_id}

