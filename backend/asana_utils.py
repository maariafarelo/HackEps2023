import os
import asana
from enum import Enum
from models import Feedback
from db import db


class Priority(Enum):
    Critical = "1206028573704637"
    High = "1206028573704634"
    Medium = "1206028573704635"
    Low = "1206028573704636"


class FeedbackType(Enum):
    Error = "1206028573704638"
    Feature = "1206028573704639"
    Enhancement = "1206028573704640"


def struct_to_send(feedback):
    tags = [Priority[feedback.priority].value, FeedbackType[feedback.feedback_type].value]
    description = feedback.description + '\n' + feedback.user_story
    data = ({"name": feedback.title, "resource_subtype": "default_task", "completed": "false", "tags": tags,
             "workspace": "1144987988736463",
             "notes": description, "projects": ["1206028568433081"]})
    return data


def send_to_asana(feedback_id):
    result = Feedback.query.filter_by(id=feedback_id).first()
    data = struct_to_send(feedback=result)
    asana_token = os.environ.get("ASANA_PAT_KEY")
    client = asana.Client.access_token(asana_token)

    result = client.tasks.create_task(data, opt_pretty=True)
    if result is None:
        return 500
    else:
        feedback = Feedback.query.get(feedback_id)
        feedback.posted = True
        db.session.commit()
        return 200
