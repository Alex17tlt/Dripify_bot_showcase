from .variables import browser, By, sleep, action, Keys
import requests
import json
from pprint import pprint

def reply(incoming_text, outgoing_msg_txt):

    # print(f'\nAbout to ask AI to reply.\n\nOutgoing msg: {outgoing_msg_txt}\n\nIncoming msgs: {incoming_text}')

    prompt = f"""
        
        I want you to generate a concise response with the ultimate goal to get user's phone number. I'll provide you with
        an outgoing message of mine, incoming messages (of the user) and guidance as to how to shape your reply.  You must strictly stick to the guidance.

    Guidance: 
    Incoming message: I’m not actively looking/I’m happy but I’m open to hearing about new/other opportunities.
    Your preferred reply: I understand! Most of the candidates I work worth aren’t actively looking. I’m happy to chat so I know what opportunities might interest you in the future. What's a good number I can reach you at?
    
    Incoming message: “I am interested in in-house opportunities.”  Keywords: inhouse, in-house, general counsel, associate general counsel
    Your preferred reply: We have in-house opportunities from time to time. In fact, we recently just filled 2 in-house positions. I’d love to discuss what type of roles you’d be interested in. What’s a good number I can reach you at?
    
    Incoming message: Which firm, which firms, which company, which law firm are you talking about ? Where in TX and what area of law?
    Your preferred reply: I’m happy to discuss it with you. We have a number of specific openings that might be a good fit, but I need to learn a little more. We also have lots of “evergreen” openings ie: always open for the right candidates. What’s a good number I can reach you at so we can chat real quick?
    
    Incoming message: It really depends on the opportunity, work environment, billable hour requirement, and compensation package.  Did you have anything specific in mind? Can you provide more specifics
    Your preferred reply: I’m happy to discuss it with you. We have a number of specific openings that might be a good fit, but I need to learn a little more. We also have lots of “evergreen” openings ie: always open for the right candidates. What’s a good number I can reach you at so we can chat real quick?
    
    Incoming message: Do you have any remote or hybrid opportunities/positions?
    Your preferred reply: Yes, we do. Happy to discuss further. What's a good number I can reach you at?
    
    Incoming message: I’m happy where I am.     I’m not interested        No thanks
    Your preferred reply: Sounds good! Most of the attorneys I work with are happy and not actively looking. But keep my information handy and let me know if/when I can ever be helpful!  Also, please share my contact information with anyone you know who may be interested in learning about opportunities. I appreciate it! 😊
    
    Incoming message: What sort of work does the firm do? Can you tell me what city or market your client is looking to open offices in?
    Your preferred reply: I’d be happy to discuss it with you on a quick call. What’s a good number I can reach you at.
    
    VERY IMPORTANT: If the person has shared their phone number, then only say: Thanks, I’ll be in touch.
    
    Here is the outgoing message:
    
    {outgoing_msg_txt}
    
    here is the incoming messages:
    
    {incoming_text}
    
    Generate a reply as if you are participating in this dialogue. Stick strictly to the examples above. If the user asks about some details like names, types of work, office locations etc, then use the examples, don't mention unreal info.
    Try to be concise. Your writing style is a perfect balance between casual and formal. Don't user line breaks, write it in one line and don't use things like Regards / Best wishes etc at the end of passage, it's unnecessary.
    Your company name is VortexLegal.
    """


    while True:

        print(f'\nSending a request to AI...')

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer <API KEY HERE>"},
                data=json.dumps({
                    "model": "meta-llama/llama-3-70b-instruct:nitro", # best
                    "messages": [
                        {"role": "user", "content": prompt},
                        {"role": "system", "content": "Your replies are concise, you stick to instructions. Your conversation style is casual, not too formal, but respectful."},
                    ]
                })
            )

            print(f'\nRequest successful')

            json_response = response.json()

            ai_response = json_response['choices'][0]['message']['content']

            # ai_response = ai_response.replace("\n", "")

            print('\n\nAI response:\n\n', ai_response)

            print(f'\nSending..')

            break
        except Exception as e:

            print(f'\nError when querying AI: {str(e)}')
            sleep(5)


    while True:
        try:
            browser.find_element(By.XPATH, "//textarea").send_keys(ai_response)
            break
        except Exception as e:
            print(f"error line 519 {str(e)}")
            sleep(5)

    sleep(1)

    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    sleep(1)
