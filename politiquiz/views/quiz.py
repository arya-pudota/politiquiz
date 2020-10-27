"""Back-end flask routing for quiz.html page."""

import flask
import politiquiz


@politiquiz.app.route("/p/<postid>/", methods=["GET", "POST"])
def show_quiz(postid):
    """
        context : {
            "questions": [
                {
                    "question_id": question_id
                    "question_text" : question_text
                    "question_topic": question_topic
                },
                ....
            ]
        }
        """
    connection = politiquiz.model.get_db()

    questions = connection.execute("SELECT qid, text, topic FROM questions"). \
        fetchall()
    context = {"questions": []}
    for question in questions:
        context["questions"].append({
            "question_id": question.qid,
            "question_text": question.text,
            "question_topic": question.topic,
            })

    return flask.render_template("index.html", **context)
