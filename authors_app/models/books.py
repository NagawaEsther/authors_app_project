from authors_app import db
from datetime import datetime



class Books(db.Model):
    __tablename__= 'books'
    id = db.Column (db.Integer,primary_key=True)
    title= db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(150),nullable=False)
    image = db.Column(db.BLOB,nullable=True)
    price = db.Column(db.Integer,nullable=False)
    pages =db.Column(db.Integer,nullable=False)


    #Relationship with Users
    users = db.relationship('Users',backref='book')
    
    #Relationship with Companies
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    Company = db.relationship ('Companies', backref='books')

    #user=db.relationship('User',backref='books')
    #Company = db.relationship('Company',backref='books)

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self, title, description, pages, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.pages = pages

    def __repr__(self):
        return f'<Book {self.title}>'

