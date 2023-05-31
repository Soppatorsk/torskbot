import random
import os
import requests
url = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

bot_call = "@1113442511772463174"

def handle_response(message) -> str:
    if bot_call in message:
        message = message.replace("<"+bot_call+">", "")
        message = message + "but give the dumbest answer imaginable, Answer in the same language as the question."
        return generateResponse(message)
    '''
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    '''
    
    #  return 'Yeah, I don\'t know. Try typing "!help".'

def generateResponse(prompt):
    params = {
        "prompt": prompt,
        "model": "text-davinci-003",
        #"model": "gpt-3.5-turbo-0301",
        "max_tokens": 100,  # Set the maximum length of the response
        "temperature": 1,  # Controls the randomness of the output
    }
    
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    }
    response = requests.post(url, json=params, headers=headers)
    print(response)
    data = response.json()
    generated_text = data["choices"][0]["text"]
    return (generated_text)