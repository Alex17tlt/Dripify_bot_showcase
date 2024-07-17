from .variables import browser,By, sleep

def check_if_inc_msgs_present():

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

        return False

    else:
        return last_incoming_messages