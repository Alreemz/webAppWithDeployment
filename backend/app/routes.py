from flask import request
from flask_restx import Namespace, Resource, fields
from .models import db, Team, Role

ns = Namespace('api', description='Team and Role operations')

team_model = ns.model('Team', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True)
})

role_model = ns.model('Role', {
    'id': fields.Integer(readOnly=True),
    'title': fields.String(required=True)
})

@ns.route('/teams')
class TeamList(Resource):
    @ns.marshal_list_with(team_model)
    def get(self):
        return Team.query.all()

    @ns.expect(team_model)
    @ns.marshal_with(team_model)
    def post(self):
        data = request.json
        team = Team(name=data['name'])
        db.session.add(team)
        db.session.commit()
        return team

@ns.route('/roles')
class RoleList(Resource):
    @ns.marshal_list_with(role_model)
    def get(self):
        return Role.query.all()

    @ns.expect(role_model)
    @ns.marshal_with(role_model)
    def post(self):
        data = request.json
        role = Role(title=data['title'])
        db.session.add(role)
        db.session.commit()
        return role

@ns.route('/assign/<int:team_id>/<int:role_id>')
class RoleAssign(Resource):
    def post(self, team_id, role_id):
        team = Team.query.get_or_404(team_id)
        role = Role.query.get_or_404(role_id)
        team.roles.append(role)
        db.session.commit()
        return {'message': f'Role {role.title} assigned to Team {team.name}'}
