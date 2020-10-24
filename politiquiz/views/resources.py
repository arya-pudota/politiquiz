"""Render the resources page."""

import flask
import politiquiz
from .helpers import save_file


@politiquiz.app.route("/u/<username>/", methods=["GET", "POST"])
def show_resources(username):