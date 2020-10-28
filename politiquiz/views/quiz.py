"""Back-end flask routing for quiz.html page."""

import flask
import politiquiz


@politiquiz.app.route("/quiz/", methods=["GET", "POST"])
def show_quiz():
    """
        context : {
            "question_topics":
            {
                "question_topic": [
                {
                    "question_id": question_id
                    "question_text" : question_text
                },
                ....
                ]
            }
        }
    """
    connection = politiquiz.model.get_db()

    questions = connection.execute("SELECT qid, text, topic FROM questions"). \
        fetchall()
    context = {"question_topics": {}}
    for question in questions:
        if not context["question_topics"][question["question_topic"]]:
            context["question_topics"][question["question_topic"]] = []

        context["question_topics"][question["question_topic"]].append({
            "question_id": question.qid,
            "question_text": question.text,
            })
    return flask.render_template("quiz.html", **context)
