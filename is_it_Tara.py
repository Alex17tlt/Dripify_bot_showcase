from .variables import browser, sleep, By

def is_it_Tara():

    # scrape the last outgoing messages
    while True:
        try:
            username = browser.find_element(By.XPATH,
                                                    "//div[@class='aside__username']").get_attribute('textContent')

            break
        except Exception as e:

            print(f"\nerror when trying to scrape current user name (Tara ot not): {str(e)}")
            sleep(5)

    if username == 'Tara Rujawitz':

        print(f'\nCurrent user is Tara Rujawitz, the bot is not going to reply to anyone')
        sleep(2)
        return True
    else:
        print(f'\nCurrent user is NOT Tara Rujawitz, the bot is going to reply')
        sleep(2)

        return False