from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_get_teacher_resources = Blueprint('principal_get_teacher_resources', __name__)

@principal_get_teacher_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of teachers"""
    teacher_list = Teacher.get_all_teacher()
    teacher_list_dump = TeacherSchema().dump(teacher_list, many=True)
    return APIResponse.respond(data=teacher_list_dump)
