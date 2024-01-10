from . import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.String(80), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Question('{self.question}', '{self.answer}', '{self.context}', '{self.date_created}')"