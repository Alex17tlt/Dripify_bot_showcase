from .variables import browser, By, sleep

def check_num_of_unread_messages(counter):

    while True:
        try:
            num_of_unread = browser.find_element(By.XPATH,  f"(//li[@aria-label='Teammate'])[{counter}]//p[contains(@style, 'unread')]").get_attribute('textContent')

            break
        except Exception as e:

            print(f'\nError when trying to get num of unread: {str(e)}')
            sleep(5)

    num_of_unread = num_of_unread.replace('Unread messages', '').strip()

    return int(num_of_unread)