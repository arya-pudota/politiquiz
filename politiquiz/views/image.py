"""Back-end flask routing for images."""
import flask
import politiquiz


@politiquiz.app.route('/uploads/<filename>')
def show_image(filename):
    """Display / route."""
    return flask.send_from_directory(politiquiz.app.config['UPLOAD_FOLDER'],
                                     filename)
