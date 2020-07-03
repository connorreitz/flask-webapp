from flask import Blueprint

bp = Blueprint('errprs', __name__)

from app.errors import handlers
