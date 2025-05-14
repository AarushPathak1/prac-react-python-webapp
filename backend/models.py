from config import db


class Contact(db.Model):
    id = db.column(db.Integer, primary_key=True)
    first_name = db.column(db.String(80), nullable=False, unique=False)
    last_name = db.column(db.String(80), nullable=False, unique=False)
    email = db.column(db.String(120), nullable=False, unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email
        }
