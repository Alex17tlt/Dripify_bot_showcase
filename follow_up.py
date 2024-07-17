from .variables import browser, By, sleep
from .scroll_msg_box import scroll_msg_box
from .is_older_than_4_days import is_older_than_4_days
from .do_followup import do_followup

def follow_up():

    scroll_msg_box()

    # identify the conversations where our message was the last one
    while True:
        try:
            messages_with_you_last = browser.find_elements(By.XPATH, "//div[@class='chat-item__inner'][.//span[@class='chat-item__you']]")

            print(f'\nFound {len(messages_with_you_last)} conversations that may need to be followed up...')

            break
        except Exception as e:
            print(f"error line 16 in follow up {str(e)}")

    """
    This variable below is going to be set to True once we identify the first conversation
    where the time is older than 4 days. Logically, all the following conversation are going
    to be even older, so there's no need to check their time then after the first one 
    has been found.
    """
    first_old_enough_found = False

    # loop through the messages and check the time
    for conversation_element in messages_with_you_last:

        try:

            """
            We need to get the time the last msg was sent, it will be used later in any case.
            """

            time_element = conversation_element.find_element(By.XPATH, './/time').get_attribute('textContent')
        except Exception as e:

            print(f'\nError while trying to find the time element to a conversation #{messages_with_you_last.index(conversation_element)}: {str(e)}')

            sleep(1)
            continue

        time_element_text = time_element.strip()

        print(f'\nConversation #{messages_with_you_last.index(conversation_element)}, last msg time: {time_element_text}')

        if first_old_enough_found is True:

            do_followup(conversation_element, time_element_text)

        else:

            if ':' in time_element_text:

                print(f'\nNot old enough to follow up as the time contains the :')

                continue
            else:

                # check if the time is older than 4 days
                is_older = is_older_than_4_days(time_element_text)

                print(f'\nIs older than 4 days ? {is_older}')

                if is_older is True:

                    first_old_enough_found = True

                    print(f'\nThe first old element has been found, all the others must be followed up by default from now.')

                    # open the conversation and process it further
                    do_followup(conversation_element, time_element_text)

    print(f'\nFOLLOWUPS COMPLETE!')
