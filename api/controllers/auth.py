from flask_restful import Resource, reqparse, abort

from api.models import User
from api.utils.errors import ValidationError


class AuthLogin(Resource):
    """docstring for AuthLogin"""

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="You need to enter your email address", required=True)
        parser.add_argument('password', type=str, help="You need to enter your password", required=True)

        args = parser.parse_args()

        email = args.get('email')
        password = args.get('password')

        try:
            token = User.validate(email, password)
            return {'token': token}
        except ValidationError as e:
            abort(400, message='There was an error while trying to log you in -> {}'.format(e.message))


class AuthRegister(Resource):
    """docstring for AuthRegister"""

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fullname', type=str, help="You need to enter your full name", required=True)
        parser.add_argument('email', type=str, help="You need to enter your email address", required=True)
        parser.add_argument('password', type=str, help="You need to enter your password", required=True)
        parser.add_argument('password_conf', type=str, help="You need to enter password again for confirmation", required=True)

        args = parser.parse_args()

        email = args.get('email')
        password = args.get('password')
        password_conf = args.get('password_conf')
        fullname = args.get('fullname')

        try:
            User.create(
                email=email,
                password=password,
                password_conf=password_conf,
                fullname=fullname
            )
            return {'message': 'Successfully created your account.'}
        except ValidationError as e:
            abort(400, message='There was an error while trying to create your account -> {}'.format(e.message))
