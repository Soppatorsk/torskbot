import random
import os
import requests
url = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

#prod
bot_call = "<@1113442511772463174>"
#dev
#bot_call = "<@1113510637507719168>"
soppatorsk_call = "@295248073649553410"
soppatorsk_praise = ["Sa någon Soppatorsk? Honom gillar jag! Han är KING!",
                     "kingen",
                     "legenden",
                     "pratar ni om kingen igen?"]

def handle_response(message) -> str:
    if bot_call in message:
        message = message.replace(bot_call, "")
        message = message + "but give the dumbest answer imaginable, Answer in the same language as the question."
        return generateResponse(message)
    if soppatorsk_call in message:
        return soppatorsk_praise[random.randint(0,len(soppatorsk_praise)-1)]
    
    #OpenAI response
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
    if response == "<Response [429]": #TODO 429 response
        "Jag är upptagen, lämna mig ifred"
    data = response.json()
    generated_text = data["choices"][0]["text"]
    return (generated_text)