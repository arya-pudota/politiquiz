"""
politiquiz index (main) view.

TODO: POST request on the older pages
        Fix some database query issues in older pages
        Phoebe: test access control issues
"""
import flask
import arrow
import politiquiz
from .helpers import get_formatted_comments, add_comment, add_like, remove_like


@politiquiz.app.route("/", methods=["GET", "POST"])
def show_index():