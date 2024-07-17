from .variables import browser, By, sleep

def sign_in(sign_in_button, username):

    print(f'\nSigning in to {username} profile...')

    # sign in
    while True:
        try:
            sign_in_button.click()
            print(f'\nClicked sign in button for user {username}')
            break
        except Exception as e:
            print(f"Error when trying to click sign in button: {str(e)}")
            sleep(5)

    sleep(5)

    # wait till loaded
    while True:
        try:
            browser.find_element(By.XPATH, "//h2[contains(.,'Statistics')]")
            break
        except Exception as e:
            print(f"error line 581 {str(e)}")
            sleep(5)

    try:
        browser.find_element(By.XPATH, "//button[@title='Close']").click()
    except:
        pass