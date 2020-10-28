"""Render the resources page."""

import flask
import politiquiz


@politiquiz.app.route("/resources/<type>/", methods=["GET"])
def show_resources(type):
    if type == 'republican':
        return flask.render_template("republican.html")

    if type == 'democratic':
        return flask.render_template("democratic.html")
