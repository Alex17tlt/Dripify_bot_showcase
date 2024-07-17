# coding: cp1252

from scripts.variables import *
from scripts.logout import logout
from scripts.sign_in import sign_in
from scripts.process_messages import process_messages
from scripts.go_to_unread import go_to_unread
from scripts.change_pagination import change_pagination
from scripts.check_num_of_unread_messages import check_num_of_unread_messages
from scripts.check_sign_in_button import check_sign_in_button
from scripts.follow_up import follow_up


def launch_scrape():

    user_response = ''

    while ('yes' not in user_response) and ('no' not in user_response):

        user_response = input('\nWould you like to follow up ?\nIt may take some time especially for users who have a large inbox.\n\nType yes if you want to follow up in addition to replying to unread messages.\nType no if not.\n\nThen hit Enter.').lower()

    while True:
        try:
            browser.get('https://app.dripify.io/team')
            break
        except Exception as e:

            print(str(e))
            sleep(10)

    print(f'\nOpened the Dripify page')

    sleep(6)

    # define the num of sign_in_buttons (WHILE IN TEAM SECTION)

    # change the "View" pagination to 50 so that the bot works with all users in the Dripify system
    change_pagination()

    # get the user's list elements which contain the sign in buttons and the unread messages count
    while True:
        try:
            user_elements = browser.find_elements(By.XPATH, '//li[@aria-label="Teammate"]')
            print(f'\nFound {len(user_elements)} users')
            break
        except Exception as e:

            print(f'\nError when trying to find user elements: {str(e)}')
            sleep(5)

    # loop through the users
    for user in range(len(user_elements)):

        counter = user + 1

        # get user's name
        while True:
            try:
                username = browser.find_element(By.XPATH, f"(//li[@aria-label='Teammate'])[{counter}]//p[contains(@style, 'name')]").get_attribute('textContent')
                break
            except Exception as e:

                print(f'\nError when trying to get username: {str(e)}')
                sleep(5)

        print(f'\nChecking {username}')

        # find the number of unread messages
        num_of_unread = check_num_of_unread_messages(counter)

        sign_in_button = check_sign_in_button(counter)

        if num_of_unread > 0:

            print(f'\nUser {username} has {num_of_unread} unread messages.')

            """
            If the sign in button is not present in the user element, then it's Jon's element, no need to sign in
            """

            if sign_in_button is False:

                print(f'\nUser {username} does not have a sign in button, going to their inbox...')

                # click Inbox
                while True:
                    try:
                        browser.find_element(By.XPATH, "//a[@href='/inbox']").click()
                        print(f'\nClicked Inbox')

                        break
                    except Exception as e:
                        print(f"error when clicking the inbox: {str(e)}")
                        sleep(5)

                sleep(4)

                if 'yes' in user_response:
                    follow_up()

                go_to_unread()
                process_messages()

                # Go back to Team section
                while True:
                     try:
                         browser.find_element(By.XPATH, "//a[@href='/team']").click()
                         break
                     except Exception as e:
                        print(f"Error when trying to go back to team section: {str(e)}")
                        sleep(5)

                sleep(4)

            else:

                sign_in(sign_in_button, username)

                # click Inbox
                while True:
                    try:
                        browser.find_element(By.XPATH, "//a[@href='/inbox']").click()
                        print(f'\nClicked Inbox')

                        break
                    except Exception as e:
                        print(f"error when clicking the inbox: {str(e)}")
                        sleep(5)

                sleep(4)

                if 'yes' in user_response:
                    follow_up()

                go_to_unread()
                process_messages()
                logout()

        else:


            """
            No incoming messages for this user, but maybe we need to follow up.
            """

            print(f'\nUser {username} has no unread messages...')

            if 'yes' in user_response:

                """
                Do the follow-up and then either go back to teams section or logout, depending on the user: Jon / not Jon
                """

                """
                Unless it's Jon, sign in, otherwise the inbox of Jon will be followed up, whereas it's someone else's turn.
                """

                # sign in if not Jon
                if 'Jon' not in username:

                    sign_in(sign_in_button, username)

                error_counter = 0

                """
                The inbox may be locked, so check how many times we cannot get to it, then just skip
                """

                skip_this_user = False

                # click Inbox
                while True:
                    try:
                        browser.find_element(By.XPATH, "//a[@href='/inbox']").click()
                        print(f'\nClicked Inbox')

                        break
                    except Exception as e:

                        if counter > 3:

                            print(f'\nProbably the inbox is locked, skip this user...')

                            skip_this_user = True

                            if 'Jon' not in username:

                                logout()
                                break

                            pass
                        else:

                            counter += 1

                            print(f"error when clicking the inbox: {str(e)}")
                            sleep(5)

                if skip_this_user is True:
                    continue
                else:

                    follow_up()

                    # if it's Jon, then go back to Teams, otherwise logout
                    if 'Jon' in username:

                        print(f"Going back to Team section from Jon's inbox...")

                        # Go back to Team section
                        while True:
                            try:
                                browser.find_element(By.XPATH, "//a[@href='/team']").click()
                                break
                            except Exception as e:
                                print(f"Error when trying to go back to team section: {str(e)}")
                                sleep(5)

                        sleep(4)

                    else:
                        logout()

launch_scrape()

print(f"\nFinished work at {datetime.datetime.now()}")