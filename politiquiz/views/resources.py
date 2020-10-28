"""Render the resources page."""

import flask
import politiquiz


@politiquiz.app.route("/u/<username>/", methods=["GET", "POST"])
def show_resources(username):
    return flask.render_template("resources.html")
