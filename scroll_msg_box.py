from .variables import browser, By, sleep

def scroll_msg_box():
    """
    This function scrolls the messages box down till the end to see how many conversations contain incoming messages and then
    loop over them.

    :return:
    """

    while True:
        try:
            list_element = browser.find_element(By.XPATH, "//ul[@aria-label='Conversations list']")
            break
        except Exception as e:
            print(f"\nError when trying to scroll down the conversations: {str(e)}")

            sleep(5)

    print(f'\nScrolling down... It may take a few minutes if there are many messages in the inbox.')

    while True:

        before_scroll = len(browser.find_elements(By.XPATH, "//div[@class='chat-item__inner']"))

        # scroll once
        while True:
            try:
                browser.execute_script("arguments[0].scroll(0, arguments[0].scrollHeight);", list_element)
                break
            except:
                pass

        sleep(0.8)

        # scrolled, but the num of dialoges remained the same -> STOP
        if before_scroll == len(browser.find_elements(By.XPATH, "//div[@class='chat-item__inner']")):

            # wait 2 more seconds, it may be that after the two additional seconds the feed will grow
            sleep(3)

            # check again
            if before_scroll == len(browser.find_elements(By.XPATH, "//div[@class='chat-item__inner']")):

                print(f'\nDone scrolling!')

                break

        else:

            # nothing, keep scrolling
            pass

    print('\nscrolled the list of conversations')