from .variables import browser, By, sleep

def check_sign_in_button(counter):

    try:
        sign_in_button = browser.find_element(By.XPATH, f"(//li[@aria-label='Teammate'])[{counter}]//div[contains(@class, 'sign-button')]/button")
        return sign_in_button
    except:
        return False