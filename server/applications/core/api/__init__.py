import logging
from flasgger import swag_from
from flask import Blueprint, request

auth = Blueprint('auth', __name__, url_prefix='/v1/auth')

from server.helpers.response import SuccessResponse, ErrorResponse  # noqa: E402
# from server.applications.core.utils.login import do_login, do_logout  # noqa: E402

############# BOXAFE AUTH ###############################


@auth.route('/login', methods=['POST'])
# @swag_from('../swagger/auth/login.yml')
def login():
    try:
        pass
        # return SuccessResponse(do_login(request))
    except Exception as err:
        logging.error(f"Failed to login: {err}")
        return ErrorResponse(err.args)


@auth.route('/logout', methods=['POST'])
# @swag_from('../swagger/auth/logout.yml')
def logout():
    try:
        pass
        # return SuccessResponse(do_logout(request))
    except Exception as err:
        logging.error(f"Failed to logout: {err}")
        return ErrorResponse('BAD_REQUEST')
