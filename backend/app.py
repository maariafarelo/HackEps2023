from flask import Flask, request, jsonify
from gpt_utils import *
from asana_utils import *
from db import db
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


CORS(app)

@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback_not_posted = Feedback.query.filter_by(posted=False).all()
    if feedback_not_posted:
        feedback_list = [{
            'id': feedback.id,
            'title': feedback.title,
            'description': feedback.description
        } for feedback in feedback_not_posted]
        return jsonify({'feedback_not_posted': feedback_list})
    else:
        return jsonify({'message': 'No high priority feedback found'}), 404


@app.route('/feedback', methods=['POST'])
def post_feedback():
    # Retrieve the body of the request
    req_body = request.json
    client = req_body.get('client')
    product = req_body.get('product')
    feedback = req_body.get('feedback')
    # Call get_gpt_response
    status = get_gpt_response(client, product, feedback)
    if status == 200:
        return {"status": status, "message": "Feedback successfully processed."}
    else:
        return {"status": status, "message": "Error processing feedback request."}


@app.route('/feedback/<int:feedback_id>', methods=['POST'])
def send_feedback_to_asana(feedback_id):
    status = send_to_asana(feedback_id)
    if status == 200:
        return {"status": status, "message": "Feedback successfully processed."}
    else:
        return {"status": status, "message": "Error processing feedback request."}
