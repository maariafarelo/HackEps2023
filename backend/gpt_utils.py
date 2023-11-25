from openai import OpenAI

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

def get_gpt_response(client, product, feedback):   
    # Manage the content received and create the prompt for ChatGPT to interpret
    prompt = "You are going to rate the feedback from a user from 0 to 10. 10 being the best and 0 being the worst. Rate on use of words, legibility and amability. Please only provide the ratings and nothing else in your response. Here is the feedback: '" + feedback + "'"

    response = get_completion(prompt)

    print(response)

    # Send prompt to ChatGPT and retrieve outputs


    # Send the json from ChatGPT to the DB

    # Return a 200 or 500 if things go right or not
    return 200


