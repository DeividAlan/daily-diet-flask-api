from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date_time = db.Column(db.DateTime, nullable=False)
    in_diet = db.Column(db.Boolean, nullable=False, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to the user
    user = db.relationship('User', backref=db.backref('meals', lazy=True))

    def __repr__(self):
        return f'<Meal {self.name}>'
    
    def to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.isoformat(),
            "in_diet": self.in_diet
        }