from flask import Flask, request
from gpt_utils import *
from asana_utils import *
app = Flask(__name__)


@app.route('/feedback', methods=['GET'])
def get_feedback():
    return 'Get feedback!'

@app.route('/feedback', methods=['POST'])
def post_feedback():
    # Retrieve the body of the request
    req_body = request.json
    client = req_body.get('client')
    product = req_body.get('product')
    feedback = req_body.get('feedback')
    print(client, product, feedback)
    # Call get_gpt_response
    status = get_gpt_response(client, product, feedback)
    if status == 200:
        return {"status": status, "message": "Feedback successfully processed."}
    else:
        return {"status": status, "message": "Error processing feedback request."}



@app.route('/feedback/<int:feedback_id>', methods=['POST'])
def send_feedback_to_asana(feedback_id):
    return 'Send feedback to Asana!'




    