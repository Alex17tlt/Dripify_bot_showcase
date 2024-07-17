from .variables import browser, By, sleep

def change_pagination():

    while True:
        try:
            pagination_button = browser.find_element(By.XPATH, '//button[@id="teamView"]')
            print(f'\nFound pagination button')
            break
        except Exception as e:

            print(f'\nError when trying to find pagination button: {str(e)}')
            sleep(5)

    pagination_text = pagination_button.get_attribute('textContent')

    if '10' in pagination_text:

        # choose a bigger pagination

        while True:
            try:
                pagination_button.click()
                sleep(1)
                break
            except Exception as e:

                print(f'\nError when trying to click pagination button: {str(e)}')
                sleep(5)

        while True:
            try:
                browser.find_element(By.XPATH, "//button[@title='50' and text()='50']").click()
                print('\nSelected pagination of 50')
                sleep(4)
                break
            except Exception as e:

                print(f'\nError when trying to click pagination of 50: {str(e)}')
                sleep(5)