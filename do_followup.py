from .variables import browser, By, sleep, action, Keys
from datetime import datetime, timedelta

date_format = "%d.%m.%Y"

def do_followup(conversation_element, time_element_text):

    """
    This function does a follow-up in a given conversation.
    If there is only one last outgoing message, then we do the followup.
    If there are more than one msgs, then we additionally check if the last time it was sent is
    older than 4 months or not. If older - follow up, otherwise nothing
    """

    # click, open
    while True:
        try:
            conversation_element.click()
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

    except:pass


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

    # check if we may send a message to them at all, otherwise skip this dialogue
    try:
        browser.find_element(By.XPATH, "//p[contains(text(), 'until they respond')]")
        print(f'\nError in this conversation, skip...')

        return
    except:pass

    # get the name of the lead
    while True:
        try:
            name = browser.find_element(By.XPATH, "//div[@class='lead-info__name wb']").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 45 when trying to extract the lead's name: {str(e)}")
            sleep(5)

    name = name.split()[0]

    followup_message = f"""Hi {name}, wanted to follow up with you. Do you have some time later this week or next week for a  call? What’s a good number I can reach you at?"""

    inc_present = False


    # check if there are any incoming messages present here
    try:
        browser.find_element(By.XPATH, "//div[@aria-label='Income message']")

        inc_present = True
        print(f'\nThere are incoming messages in this conversation.')
    except:

        print(f'\nThere are NO incoming messages in this conversation.')


    # depending on the presence of inc msgs, we need to modify the xpath
    if inc_present is True:

        last_outgoing_msgs = browser.find_elements(By.XPATH, "//div[@aria-label='Income message'][last()]/following::div[@aria-label='Outcome message']")
    else:
        last_outgoing_msgs = browser.find_elements(By.XPATH, "//div[@aria-label='Outcome message']")

    if len(last_outgoing_msgs) == 1:

        print(f'\nThere is only one outgoing message, doing a follow-up...')

        # do a follow-up
        while True:
            try:
                browser.find_element(By.XPATH, "//textarea").send_keys(followup_message)
                break
            except Exception as e:
                print(f"error line 519 {str(e)}")
                sleep(5)

        sleep(0.5)

        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

        sleep(1)

    else:

        print(f'There is more than one outgoing message, check if the date is older than 4 months')

        if ':' in time_element_text:
            print(': is in the datetime, skip...')
        else:
            given_date = datetime.strptime(time_element_text, date_format)

            # Get the current date
            current_date = datetime.now()

            # Calculate the difference
            date_difference = current_date - given_date

            # Check if the difference is more than 4 days
            is_older_than_4_months = date_difference > timedelta(days=120)

            if is_older_than_4_months is True:

                print(f'\nThis conversation is at least 4 months old, do a follow up')

                # follow up
                while True:
                    try:
                        browser.find_element(By.XPATH, "//textarea").send_keys(followup_message)
                        break
                    except Exception as e:
                        print(f"error line 519 {str(e)}")
                        sleep(5)

                sleep(0.5)

                action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

                sleep(1)
            else:

                print(f'\nThis conversation is not 4 months old, skipping it...')
