from .variables import browser, By, sleep
from .scroll_msg_box import scroll_msg_box
from .get_unread_conversations_elements import get_unread_conversation_elements
from .check_if_inc_msgs_present import check_if_inc_msgs_present
from .scrape_data import scrape_data
from .is_interested import is_interested
from .reply import reply
from .write_to_sheet import write_to_sheet
from .is_it_Tara import is_it_Tara
from .is_phone_number_present import is_phone_number_present


def process_messages():

    # TODO: do not reply if the user has sent their phone nubmer already
    is_tara = is_it_Tara()

    scroll_msg_box()

    conversation_elements = get_unread_conversation_elements()

    for dialogue in conversation_elements:

        # click, open
        while True:
            try:
                dialogue.click()
                break
            except Exception as e:
                print(f"\nerror when trying to open a dialogue: {str(e)}")
                sleep(5)

        sleep(1.5)

        """
           There may be a warning here: "Your LinkedIn messages cannot be retrieved from LinkedIn at the moment.
       Please try again in a few hours" - if it's there, continue
           """

        try:

            browser.find_element(By.XPATH, '//div[@class="conversation__error"]')
            print(f'\nError in this conversation, skip...')
            return

        except:
            pass

        counter = 0

        # wait to load
        while True:

            try:
                browser.find_element(By.XPATH, "//div[@class='msg__content']")
                break

            except Exception as e:
                print(f"error line 32 in do_followup {str(e)}")

                sleep(2)

                counter += 1

                if counter > 4:

                    # check the msg error again
                    try:

                        browser.find_element(By.XPATH, '//div[@class="conversation__error"]')
                        print(f'\nError in this conversation, skip...')
                        return

                    except Exception as e:

                        print(f'\nError line 67 in do_followup when waiting for msgs to load: {str(e)}')
                        sleep(20)

        inc_msgs = check_if_inc_msgs_present()

        # there may be a case when there are actually no incoming messages, even though it says that there are
        if inc_msgs is not False:

            if len(inc_msgs) > 0:

                print(f'\nThere are {len(inc_msgs)} incoming messages from this lead.')
                sleep(1)

                # get the incoming text
                incoming_text = str()

                # get the text of inc msgs
                for inc_msg in inc_msgs:
                    incoming_text = f'{incoming_text}\n{inc_msg.get_attribute("textContent")}'

                # scrape data
                scraped_data = scrape_data()

                # scrape the last outgoing messages
                while True:
                    try:
                        outgoing_msg_txt = browser.find_element(By.XPATH, "(//div[@aria-label='Outcome message']//p)[last()]").get_attribute('textContent')

                        print(f'\nFound last outgoing msg')
                        break
                    except Exception as e:

                        print(f"error line 155 {str(e)}")

                # check if the person sounds interested
                if is_interested(incoming_text, outgoing_msg_txt) is True:

                    write_to_sheet('interested', scraped_data)
                else:
                    write_to_sheet('not interested', scraped_data)

                # reply, but don't reply for Tara Rujawitz and if phone number is present
                if is_tara is False and is_phone_number_present(incoming_text) is False:
                    reply(incoming_text, outgoing_msg_txt)

        else:
            print(f'\nThere are no incoming messages in this dialogue..')
            sleep(2)