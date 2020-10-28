"""
politiquiz index (main) view.
"""
import flask
import politiquiz


@politiquiz.app.route("/", methods=["GET", "POST"])
def show_index():
    return flask.render_template("index.html")
