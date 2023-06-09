from flask_sqlalchemy import SQLAlchemy


# initialise the database
db = SQLAlchemy()

# create a model for the table esp2
class esp2(db.Model) :
    ID = db.Column(db.Integer, primary_key=True)
    Moisture = db.Column(db.Integer)
    temperature = db.Column(db.Date)
    humidity = db.Column(db.Integer)
    light = db.Column(db.Integer)

    def __repr__(self):
        return f'id: {self.ID}, Moisture: {self.Moisture}, temperature: {self.temperature}, humidity: {self.humidity}, light: {self.light}'
    

