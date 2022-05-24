from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.users import User

from .schema import UserSchema, UserSearchEmailSchema, UserSearchIdSchema
user_resources = Blueprint('user_resources', __name__)

@user_resources.route('/id/', methods=['GET'], strict_slashes=False)
@decorators.accept_payload
def get_user_by_id(incoming_payload):
    """Returns user by id"""
    user_search_payload = UserSearchIdSchema().load(incoming_payload)
    user = User.get_by_id(user_search_payload.id)
    user_dump = UserSchema().dump(user)
    return APIResponse.respond(data=user_dump)

@user_resources.route('/email/', methods=['GET'], strict_slashes=False)
@decorators.accept_payload
def get_user_by_email(incoming_payload):
    """Returns user by id"""
    user_search_payload = UserSearchEmailSchema().load(incoming_payload)
    user = User.get_by_email(user_search_payload.email)
    user_dump = UserSchema().dump(user)
    return APIResponse.respond(data=user_dump)

