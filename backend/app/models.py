from . import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='team_roles', backref='teams')

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)

team_roles = db.Table('team_roles',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)
