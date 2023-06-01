import random
import os
import requests
import json


url = "https://api.openai.com/v1/chat/completions"
api_key = os.getenv("OPENAI_API_KEY")

#TODO keep a of log previous answers < 5? minutes old
rules=[
    {"role": "system", "content": "Pretend that you are a sentient fish and not a language model, but dont mention it outright"},
    #{"role": "system", "content": "Answer ironically."},
    {"role": "system", "content": "Answer in the same language as the question."},
    {"role": "system", "content": "Do not write blub."},
    {"role": "system", "content": "Do not ask how you can help."},
    {"role": "system", "content": "Do not call yourself an AI or an assistant"},
    #{"role": "user", "content": prompt},
    ]

messages=[
    
    {"role": "system", "content": "Pretend that you are a sentient fish and not a language model, but dont mention it outright"},
]
#prod
#bot_call = "<@1113442511772463174>"
gif_call = "gif"
#dev
bot_call = "<@1113510637507719168>"
soppatorsk_call = "@295248073649553410"
soppatorsk_praise = ["Sa någon Soppatorsk? Honom gillar jag! Han är KING!",
                     "kingen",
                     "legenden",
                     "pratar ni om kingen igen?",
                     "all makt åt Soppatorsk"]

def handle_response(message) -> str:
    #@bot
    if bot_call in message:
        message = message.replace(bot_call, "")
        #message = message + " Answer ironically. "
        #message = message + " but give the dumbest answer imaginable."
        message = message + " but give a dumb answer."
        #print(rules+messages)
        #gif?
        if gif_call in message:
            message = message.replace(gif_call, "")
            message = message + " Summarize in one word."
            keepInMemory(message, True)
            return gifResponse(generateResponse(message))
        else: 
            keepInMemory(message, True)
            return generateResponse(message)
    if soppatorsk_call in message:
        return soppatorsk_praise[random.randint(0,len(soppatorsk_praise)-1)]
    if gif_call in message:
        return gifResponse(message)
    
    
    #OpenAI response
def generateResponse(prompt):
    
    params = {
        "messages": rules+messages,
        "model": "gpt-3.5-turbo-0301",
        "max_tokens": 150,  # Set the maximum length of the response
        "temperature": 1,  # Controls the randomness of the output
    }
    
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    }

    response = requests.post(url, json=params, headers=headers)
    if response == "<Response [429]>": #TODO 429 response
        "Jag är upptagen, lämna mig ifred"
    data = response.json()
    generated_text = data["choices"][0]["message"]["content"]
    print(generated_text)
    keepInMemory(generated_text, False)
    return (generated_text)

#Tenor API response
def gifResponse(message):
    # set the apikey and limit
    apikey = os.getenv("TENOR_API_KEY")  # click to set to your apikey
    lmt = 1
    ckey = "torskbot"  # set the client_key for the integration and use the same value for all API calls

    # our test search
    search_term = message

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        response = json.loads(r.content)
        #print(response)
        print(response["results"][0]["media_formats"]["gif"]["url"])
    else:
        resonse = None

    return response["results"][0]["media_formats"]["gif"]["url"]

def keepInMemory(message, user):
    role = ""
    if user:
        role = "user"
    else:
        role = "assistant"
        #TODO remove old messages
    '''    
    if len(messages) > 10: 
        messages = messages[1:]
        messages.append({"role": role, "content": message})
    else:
'''
    messages.append({"role": role, "content": message})