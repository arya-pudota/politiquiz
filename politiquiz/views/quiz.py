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
    questions = connection.execute("SELECT qid, text, topic, lean, text_detail FROM questions"). \
        fetchall()

    if flask.request.method == "POST":
        political_score = 0
        question_answers = dict(flask.request.form)
        num_answers = len(question_answers)
        for answer in question_answers:
            for question in questions:
                if int(answer) == question["qid"]:
                    if question["lean"] == "Conservative":
                        political_score += int(question_answers[answer])
                    elif question["lean"] == "Liberal":
                        political_score += 6 - int(question_answers[answer])
                    break
        political_score = political_score / num_answers
        if political_score > 3:
            return flask.redirect(flask.url_for('show_resources', type="republican"))
        else:
            return flask.redirect(flask.url_for('show_resources', type="democratic"))


    context = {"question_topics": {}}
    for question in questions:
        if question["topic"] not in context["question_topics"]:
            context["question_topics"][question["topic"]] = []

        context["question_topics"][question["topic"]].append({
            "question_id": question["qid"],
            "question_text": question["text"],
            })

        if question['text_detail']:
            context['question_topics'][question['topic']][-1]['text_detail'] = question['text_detail']
            
    return flask.render_template("quiz.html", **context)
