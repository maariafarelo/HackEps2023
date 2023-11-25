from flask import Flask

app = Flask(__name__)


@app.route('/feedback', methods=['GET'])
def get_feedback():
    return 'Get feedback!'

@app.route('/feedback', methods=['POST'])
def post_feedback():
    return 'Post feedback!'


@app.route('/feedback/<int:feedback_id>', methods=['POST'])
def send_feedback_to_asana(feedback_id):
    return 'Send feedback to Asana!'




    