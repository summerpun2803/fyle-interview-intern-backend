
from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.assignments import AssignmentStateEnum


from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_principal_assignments(p):
    """Returns list of submitted and graded assignments"""
    principal_assignments = Assignment.filter(Assignment.state.in_([AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED])).all()
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_regrade_assignment(p, incoming_payload):
    """Grade or regrade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    regrade_assignment = Assignment.update_grade(_id = grade_assignment_payload.id , grade = grade_assignment_payload.grade)
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(regrade_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
