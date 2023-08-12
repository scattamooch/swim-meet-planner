from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Swimmer(db.Model, SerializerMixin):
    __tablename__ = "swimmers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))

    #relationships
    times = db.relationship("Time", back_populates="swimmer")
    event = association_proxy("times", "event")
    team = db.relationship("Team", back_populates="swimmer")


    #validations

    def __repr__(self):
        return f'<Swimmer {self.id}: {self.name}>'
    

class Team(db.Model, SerializerMixin):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #relationships
    swimmer = db.relationship("Swimmer", back_populates="team")

    #validations

    def __repr__(self):
        return f'<Team {self.id}: {self.name}>'
        

class Event(db.Model, SerializerMixin):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #relationships
    times = db.relationship("Time", back_populates="event")
    swimmer = association_proxy("times", "swimmer")

    #validations

    def __repr__(self):
        return f'<Event {self.id}: {self.name}>'
    
    
class Time(db.Model, SerializerMixin):
    __tablename__ = "times"

    id = db.Column(db.Integer, primary_key=True)
    swimmer_id = db.Column(db.Integer, db.ForeignKey("swimmers.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    time = db.Column(db.Numeric(precision=5, scale=2))

    #relationships
    swimmer = db.relationship("Swimmer", back_populates="times")
    event = db.relationship("Event", back_populates="times")

    #validations

    def __repr__(self):
        return f'<Time {self.id}: {self.time}>'