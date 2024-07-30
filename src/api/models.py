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

class Users(db.model):
    __tablename__ = "users"
    id = db.column(db.integter, primary_key=True)
    username = db.column(db.string(60), unique=True, nullable=False)
    firstname = db.column(db.string(60), unique=True, nullable=False)
    laststname = db.column(db.string(60), unique=True, nullable=False)
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

    
class Comments(db.model):
    __tablename__ = "comments"
    id = db.column(db.integter, primary_key=True)
    comment_text = db.column(db.string, nullable=False)
    author_id = db.column(db.integer, db.ForeingKey['users_id'])
    author_to = db.relationship('Users', foreign_keys=[author_id])
    post_id = db.column(db.integer, db.ForeingKey('posts.id'))
    post_to = db.relationship('Posts', foreign_keys=[post_id], backref=db.backref('comment_to', lazy='select'))


class Posts(db.model):
    __tablename__ = "posts"
    id = db.Column(db.integter, primary_key=True)
    user_id = db.column(db.integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('post_to', lazy='select'))


class Followers(db.model):
    __tablename__ = "followers"
    user_from_id = db.column(db.integer, db.ForeignKey('users.id'))
    user_from_to = db.relationship('Users', foreign_keys=[user_from_id])
    user_to_id = db.column(db.intege, db.ForeignKey('users.id'))
    user_to_to = db.relationship('Users' foreign_keys=[user_to_id])


class Medias(db.model):
    __tablename__ = "medias"
    id = db.column(db.integter, primary_key=True)
    comment_text = db.column(db.string, nullable=False)
    author_id = db.column(db.integer)
    post_id = db.column(db.integer)


