from app import db 

class User(db.Model):
  id = db.Column()
  nickname = db.Column()
  email = db.Column()

  def __repr__(self):
    
  