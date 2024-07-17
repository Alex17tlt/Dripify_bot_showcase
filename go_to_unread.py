from .variables import browser, By, sleep

def go_to_unread():

    # click Unread
    counter = 0
    while True:
        try:
            browser.find_element(By.XPATH, "//button[@id='filter-unread']").click()
            break
        except Exception as e:

            counter += 1

            if counter > 3:
                print(f'\nNo messages for this user...')
                return
            else:
                sleep(0.5)

    print(f'\nClicked Unread')

    sleep(3)