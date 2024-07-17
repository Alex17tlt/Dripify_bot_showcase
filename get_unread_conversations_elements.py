from .variables import browser, By

def get_unread_conversation_elements():

    while True:
        try:
            unread_msgs = browser.find_elements(By.XPATH, "//div[@class='chat-item__inner']")
            break
        except Exception as e:
            print(f"error line 123 {str(e)}")

    return unread_msgs