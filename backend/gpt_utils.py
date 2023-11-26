from openai import OpenAI
import re
import json
import os
from dotenv import load_dotenv, find_dotenv


def get_completion(prompt, model="gpt-3.5-turbo"):

    load_dotenv(find_dotenv())
    client = OpenAI(api_key=os.environ.get("OPEN_AI_API_KEY"))
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)

    return response

def get_gpt_response(client, entity, feedback):   
    # Manage the content received and create the prompt for ChatGPT to interpret
    prompt = "At the end of this prompt I will send you the feedback that a user has given to a certain product of our enterprise group. I will also send you which entity inside this group the user is refering to with this feedback. So that you have more context, let me clue you in the enterprise group: The group is called 'InGroup' and it is composed by a variety of entities, which I will list now one by one. INTECH3D: A leader in 3D impression and official distributor of main brands in the additive manufacturing market. Invelon: Specialized in the development of customized Virtual, Augmented and Mixed Reality solutions for companies. Origen: Company specialized in customized Software solutions, focused on offering exceptional user experiences and high quality code. Innitia: Marketing agency that integrates new marketing technologies, such as Artificial Intelligence, for leading companies. XRShop: Online store specialized in Augmented Reality and Gaming. IngameVR: Virtual reality game zone. Print&GO: Leading multi-brand managed services solution for 3D printers, allowing them to be controlled remotely and in real time. Aurora: Software to validate engineering projects in Virtual Reality. Fabrex: Digitization platform for manufacturing companies from order management to production optimization with AI. After this context-awareness, you should be able to have more context on the issue that the user is facing, or the enhancement that they are asking by understanding the entity to which they refer with their feedback. You will have the information at the end of this prompt. Now, I need you to respond to this message in a really specific way. I do not want you to give me any extra information that I don't ask for. I need you to return a json-like response. That is, starting with { and ending with } and having pairs of key-value in it. The first key is the 'title'. The title is a brief description of the problem, enhancement or feature that the user is stating in the feedback in a straight-forward, IT manner. The title must always be less than 100 chars. The next key is the 'priority'. The priority can take 4 different values: Low, Medium, High and Critical. With the context I provided and the wording on the user's feedback, you must categorize this feedback into one of the four values possible for priority. The next on is the 'description'. The description is an enhanced version of the user prompt. You must remove any unnecessary information and add valuable aspects for the developers that will read this enhanced version. Keep in mind that this is the way the developers will know what the user wants. Do not exceed 300 chars by any means in this field. The next key is the 'user_story'. The user story must follow a specific pattern, well known in software development. It must describe the functionality, enhancement or error to be fixed or added perfectly following the convention of 'As a [role] who ... I want ... so that ...'. For example, a great user story is 'As a user who uses google maps, I want to be able to search directions so that I can get around easily'. The last key is 'feedback_type'. The feedback type falls into one of three categories: Error, Feature or Enhancement. From the user description and the context I provided you must be able to identify if the user is reporting an error, is asking for a new feature to be added or is requesting an enhancement on an existing feature. Always provide one of the three in the value for this key and only one. That will be all that I need. I will now give you the user feedback under 'Feedback' and the entity under 'entity'."
    if feedback != None and entity != None:
        prompt += "\n\nFeedback: " + feedback  + "\n\nEntity: " + entity + "\n\n"
    else:
        return 400

    response = get_completion(prompt)
    pattern = r'content=\'(.*?)\''
    match = re.search(pattern, str(response))
    if match:
        # Remove the \n
        content_value = re.sub(r'\\n', '', match.group(1))
        data = json.loads(content_value)
        for key, value in data.items():
            # Insert the data in the database
            print(f"{key}: {value}")
        return 200
    else:
        return 400


    # Return a 200 or 500 if things go right or not


