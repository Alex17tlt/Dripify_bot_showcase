from .variables import browser, By, sleep

def logout():

    # log out
    while True:
        try:
            browser.find_element(By.XPATH, "//div[@class='header-menu__btn']").click()
            break
        except Exception as e:
            print(f"error line 306 {str(e)}")
            sleep(5)

    sleep(1)

    # click logout
    while True:
        try:
            browser.find_element(By.XPATH, "//button[contains(.,'Log out')]").click()
            break
        except Exception as e:
            print(f"error line 306 {str(e)}")
            sleep(5)

    sleep(5)

    # check the page loaded
    while True:
        try:
            browser.find_element(By.XPATH, "//a[contains(.,'Jon Broder')]")
            break
        except Exception as e:
            print(f"error line 451 {str(e)}")
            sleep(5)

