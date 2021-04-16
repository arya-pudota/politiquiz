"""Back-end flask routing for topics.html page."""

import flask
import politiquiz


@politiquiz.app.route("/topics/", methods=["GET", "POST"])
def show_topics():
    """
        context : {
            "topics": {}
        }
    """
    topics = []
    connection = politiquiz.model.get_db()
    questions = connection.execute("SELECT qid, text, topic, lean, text_detail FROM questions"). \
        fetchall()
    for question in questions:
        if question["topic"] not in topics:
            topics.append(question["topic"])
    context = {"topics": topics}

    if flask.request.method == "POST":
        # get all the topics they selected and send those over to quiz.py
        selected_topics = ""
        for topic in topics:
            if flask.request.form.get(topic):
                selected_topics += topic
                selected_topics += ","
        return flask.redirect(flask.url_for('show_quiz', topics=selected_topics))

    return flask.render_template("topics.html", **context)
