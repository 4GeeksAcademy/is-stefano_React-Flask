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
         return f'<User {self.email} - {self.username}>'

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
    


