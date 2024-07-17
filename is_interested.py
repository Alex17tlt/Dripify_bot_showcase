from .variables import browser, By, sleep
import requests
import json
from pprint import pprint

def is_interested(incoming_text, outgoing_msg_txt):

    print(f'\nAbout to ask AI if this person is interested.\n\nOutgoing msg: {outgoing_msg_txt}\n\nIncoming msgs: {incoming_text}')

    prompt = f"""
    I'm going to provide you with a snippet of a dialogue. There's an outgoing message (it was sent first), and a series of incoming messages that followed.
    You have to determine whether or not the sender of the incoming messages sounds interested to talk further, find out more etc.
    If the person sounds interested, respond only with "Yes, interested". If not, then "No, not interested".
    
    Also: if they send their phone number, it means they are interested.
    
    Below are some examples of incoming  messages that you could classify as "No, not interested":
    
    'I’m actually looking for help in my marketing dept if you’re interested'
    
    'Will do. Thanks!'
    
    'I’m not looking for a new role at this time'
    
    'Congrats on your work anniversary!'
    
    'Thanks Jonathan, it’s nice to meet you here.'
    
    'Thank you, Jonathan L.'
    
    'did you actually research me, my background, and my firm, before sending this to me?'
    
    'I just don’t think that I would be a fit for any of these roles'
    
    'I’m not a good fit for the role, however a colleague would be perfect.'
    
    'I'm happy to connect'
    
    'I just left my firm in January and started a solo practice.  Pretty acrimonious split.  So not interested in another firm at this time.  I might consider in house if it were the right opportunity.'
    
    Now, Here is the outgoing message:

    {outgoing_msg_txt}
    
    And here is the incoming messages:

    {incoming_text}
    
    Respond only with "Yes, interested" or "No, not interested".
    """

    response = requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": f"Bearer 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"},
      data=json.dumps({
        "model": "microsoft/wizardlm-2-8x22b",
        "messages": [
          { "role": "user", "content": prompt }
        ]
      })
    )

    json_response = response.json()

    ai_response = json_response['choices'][0]['message']['content']

    print('\n\nAI response:\n\n', ai_response)

    sleep(3)

    if 'Yes' in ai_response:
        return True
    else:
        return False
