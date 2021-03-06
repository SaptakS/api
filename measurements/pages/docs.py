import os
from flask import Blueprint, render_template, current_app, request

from measurements.config import BASE_DIR

# prefix: /api
api_docs_blueprint = Blueprint("api_docs", "measurements")


@api_docs_blueprint.route("/", methods=["GET"])
def api_docs():
    return render_template("api.html")
