from app import db

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String, unique=True)
    car1 = db.Column(db.String)
    color1 = db.Column(db.String)
    car2 = db.Column(db.String)
    color2 = db.Column(db.String)
    car3 = db.Column(db.String)
    color3 = db.Column(db.String)

    def __init__(self, client, car1, color1, car2, color2, car3, color3):
        self.client = client
        self.car1 = car1
        self.color1 = color1
        self.car2 = car2
        self.color2 = color2
        self.car3 = car3
        self.color3 = color3

