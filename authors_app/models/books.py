from authors_app import db
from datetime import datetime



class Books(db.Model):
    __tablename__= 'books'
    id = db.Column (db.Integer,primary_key=True)
    title= db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(150),nullable=False)
    image = db.Column(db.BLOB,nullable=True)
    price=db.Column(db.Integer,nullable=False)
    price_unit = db.Column(db.Integer,nullable=False,default='UGX')
    publication_date=db.Column(db.Date,nullable=False)
    isbn=db.Column(db.String(30),nullable=True,unique=True)
    genre=db.Column(db.String(50),nullable=False)
    pages =db.Column(db.Integer,nullable=False)
    users = db.relationship('Users',backref='book')#Relationship with Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #Relationship with Companies
    Company = db.relationship ('Companies', backref='books')
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    #user=db.relationship('User',backref='books')
    #Company = db.relationship('Company',backref='books)
    
    def __init__(self, title,price, description, pages, user_id,price_unit,publication_date,isbn,company_id,image,genre):
        super(Books,self).__init__()
        self.title = title
        self.description = description
        self.price=price
        self.user_id = user_id
        self.price_unit=price_unit
        self.pages = pages
        self.isbn=isbn
        self.publication_date=publication_date
        self.image=image
        self.genre=genre
        self.company_id=company_id



    def __repr__(self) -> str :
        return f'<Book {self.title}>'

