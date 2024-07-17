from .variables import browser, By, sleep

def check_if_phone_sent():

    """
    If this function returns "Yes", then the bot does not reply to the user, because VL user has already received their phone number.
    The bot only has to scrape the data
    :return:
    """

    # get name just for logging purposes within this function
    while True:
        try:
            name = browser.find_element(By.XPATH, "//div[@class='lead-info__name wb']").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 170 {str(e)}")

    # check if the last msg of the owner was  "what's a good number i can reach you at?" so that we don't ask for it again
    while True:
        try:
            outgoing_msgs = browser.find_elements(By.XPATH, "//div[@aria-label='Outcome message']//p")
            break
        except Exception as e:

            print(f"error line 155 {str(e)}")

    for i in outgoing_msgs:

        outgoing_msg = i.get_attribute('textContent')

        if "number to reach you at?" in outgoing_msg or "number I can reach you" in outgoing_msg:

            print(f'\nDialogue with: {name}. Last msg was one of the VL user asking for a phone number...')
            sleep(1)

            # get the last msg_texts
            while True:
                try:
                    last_incoming_messages = browser.find_elements(By.XPATH,
                                                                   "(//div[@aria-label='Outcome message'])[last()]//following-sibling::div[@aria-label='Income message']//div[@class='msg__content']//p")
                    break
                except Exception as e:
                    print(f"error line 152 {str(e)}")

            # may be 0 messages, 'cause the owner's one is the last one
            if len(last_incoming_messages) == 0:

                print(f'\nDialogue with: {name}. No incoming messages in this dialogue... continue')
                sleep(2)
                return 'Yes, without messages'

            else:
                return 'Yes, with messages'

        else:
            return 'No'