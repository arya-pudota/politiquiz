"""Back-end flask routing for quiz.html page."""

import flask
import arrow

import politiquiz
from .helpers import get_formatted_comments, add_comment, add_like, remove_like


@politiquiz.app.route("/p/<postid>/", methods=["GET", "POST"])
def show_quiz(postid):