from .variables import browser,By, sleep
import datetime

big_law_list = ['Akerman LLP', 'Akin, Gump, Strauss, Hauer & Feld, LLP', 'Allen Matkins Leck Gamble Mallory & Natsis LLP', 'Alston & Bird LLP', 'Amundsen Davis LLC', 'ArentFox Schiff LLP', 'Arnall Golden Gregory LLP', 'Arnold & Porter Kaye Scholer LLP', 'Atkinson, Andelson, Loya, Ruud & Romo', 'Baker & Hostetler LLP', 'Baker Botts LLP', 'Barnes & Thornburg LLP', 'Bass, Berry & Sims PLC', 'Benesch Friedlander Coplan & Aronoff LLP', 'Best Best & Krieger LLP', 'Blank Rome LLP', 'Bracewell LLP', 'Bradley Arant Boult Cummings LLP', 'Bricker Graydon LLP', 'Buchalter PC', 'Buchanan Ingersoll & Rooney PC', 'Butler Snow LLP', 'Cadwalader, Wickersham & Taft LLP', 'Carlton Fields PA', 'Chapman and Cutler LLP', 'Chiesa Shahinian & Giantomasi PC', 'Cipriani & Werner PC', 'Clark Hill PLC', 'Cleary, Gottlieb, Steen & Hamilton', 'Clifford Chance', 'Cole Schotz', 'Cooley LLP', 'Covington & Burling LLP', 'Cozen O Connor', 'Cravath, Swaine & Moore LLP', 'Crowell & Moring LLP', 'Cullen and Dykman LLP', 'Davis Polk & Wardwell LLP', 'Davis Wright Tremaine LLP', 'Day Pitney LLP', 'Debevoise & Plimpton LLP', 'Dechert LLP', 'Dentons', 'Dickie, McCamey & Chilcote, P.C.', 'Dickinson Wright PLLC', 'Dinsmore & Shohl LLP', 'DLA Piper', 'Dorsey & Whitney LLP', 'Duane Morris LLP', 'Epstein Becker & Green PC', 'Faegre Drinker Biddle & Reath LLP', 'Fennemore Craig PC', 'Fenwick & West LLP', 'Fish & Richardson P.C.', 'Foley & Lardner LLP', 'Foley Hoag LLP', 'Fox Rothschild LLP', 'Fredrikson & Byron PA', 'Freshfields Bruckhaus Deringer', 'Fried, Frank, Harris, Shriver & Jacobson LLP', 'Frost Brown Todd LLP', 'Gibson, Dunn & Crutcher LLP', 'Goodwin Procter LLP', 'Greenberg Traurig LLP', 'Gunster', 'Hanson Bridgett LLP', 'Haynes and Boone, LLP', 'Hodgson Russ LLP', 'Hogan Lovells', 'Holland & Knight LLP', 'Honigman LLP Attorneys & Counselors', 'Hunton Andrews Kurth', 'Husch Blackwell LLP', 'Ice Miller LLP', 'Jackson Walker LLP', 'Jenner & Block LLP', 'Jones Day', 'K & L Gates LLP', 'Katten Muchin Rosenman LLP', 'Kean Miller LLP', 'Kelley Drye & Warren LLP', 'Kilpatrick Townsend & Stockton LLP', 'King & Spalding LLP', 'Kirkland & Ellis LLP', 'Kramer Levin Naftalis & Frankel LLP', 'Kutak Rock LLP', 'Latham & Watkins LLP', 'Lippes Mathias LLP', 'Loeb & Loeb LLP', 'Lowenstein Sandler LLP', 'Manatt, Phelps & Phillips LLP', 'Mayer Brown LLP', 'Maynard Nexsen PC', 'McAngus Goudelock & Courie LLC', 'McDermott Will & Emery LLP', 'McDonald Hopkins LLC', 'McGuireWoods LLP', 'Michael Best & Friedrich LLP', 'Milbank LLP', 'Miles & Stockbridge PC', 'Mintz, Levin, Cohn, Ferris, Glovsky and Popeo P.C.', 'Moore & Van Allen PLLC', 'Morgan, Lewis & Bockius LLP', 'Morrison & Foerster LLP', 'Munger, Tolles & Olson LLP', 'Nelson Mullins Riley & Scarborough LLP', 'Nixon Peabody LLP', 'Norton Rose Fulbright', 'O Melveny & Myers LLP', 'O’Hagan Meyer', 'Offit Kurman', 'Parker Poe Adams & Bernstein LLP', 'Patterson, Belknap, Webb & Tyler LLP', 'Paul Hastings LLP', 'Paul, Weiss, Rifkind, Wharton & Garrison LLP', 'Perkins Coie LLP', 'Phelps Dunbar LLP', 'Pillsbury Winthrop Shaw Pittman LLP', 'Polsinelli PC', 'Proskauer Rose LLP', 'Pryor Cashman LLP', 'Quarles & Brady LLP', 'Quinn Emanuel Urquhart & Sullivan, LLP', 'Reinhart Boerner Van Deuren SC', 'Rimon PC', 'Rivkin Radler LLP', 'Robbins Geller Rudman & Dowd LLP', 'Robinson & Cole LLP', 'Ropes & Gray LLP', 'Saul Ewing LLP', 'Schulte Roth & Zabel LLP', 'Seyfarth Shaw LLP', 'Sheppard Mullin', 'Shook, Hardy & Bacon LLP', 'Sidley Austin LLP', 'Simpson Thacher & Bartlett LLP', 'Skadden, Arps, Slate, Meagher & Flom LLP and Affiliates', 'Snell & Wilmer LLP', 'Spencer Fane', 'Squire Patton Boggs', 'Steptoe & Johnson PLLC', 'Steptoe LLP', 'Sterne Kessler Goldstein Fox', 'Stinson LLP', 'Stradley Ronon Stevens & Young LLP', 'Sullivan & Cromwell LLP', 'Susman Godfrey L.L.P.', 'Taft Stettinius & Hollister LLP', 'Thompson Coburn LLP', 'Thompson Hine LLP', 'Troutman Pepper Hamilton Sanders LLP', 'Tucker Ellis LLP', 'UB Greensfelder LLP', 'Vedder Price', 'Venable LLP', 'Vinson & Elkins LLP', 'Vorys, Sater, Seymour and Pease, LLP', 'Wachtell, Lipton, Rosen & Katz', 'Warner Norcross & Judd LLP', 'Weil Gotshal & Manges LLP', 'White & Case LLP', 'White and Williams LLP', 'Williams & Connolly LLP', 'Williams, Mullen', 'Willkie Farr & Gallagher LLP', 'Wilmer Cutler Pickering Hale and Dorr LLP', 'Winstead PC', 'Winston & Strawn LLP', 'Womble Bond Dickinson (US) LLP']

def scrape_data():

    # default values that change based on big law presence of the company the lead works for

    assign_to = 'Brooke'
    is_big_law = ''


    # get the last msg_text
    while True:
        try:
            msg_text = browser.find_element(By.XPATH, "(//div[@class='msg__content'])[last()]").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 162 {str(e)}")

    # get name
    while True:
        try:
            name = browser.find_element(By.XPATH, "//div[@class='lead-info__name wb']").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 170 {str(e)}")
            sleep(5)

    # get current account name (who we are)
    while True:
        try:
            account_name = browser.find_element(By.XPATH, "//div[@class='aside__username']").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 298 {str(e)}")

            sleep(5)

    try:

        # get company
        company = browser.find_element(By.XPATH, "//div[text()='Company']//following-sibling::div").get_attribute(
            'textContent')
    except Exception as e:

        company = '-'

    # if the company name is a valid one and it's also on the big law list
    if company != '-' and any(company in elem for elem in big_law_list):

        assign_to = 'Tara'
        is_big_law = 'Yes'

    # get email
    try:
        email = browser.find_element(By.XPATH,
                                     "//span[@class='fe-item__email']").get_attribute(
            'textContent')
    except Exception as e:

        email = '-'

    # get title
    while True:
        try:
            title = browser.find_element(By.XPATH,
                                         "//div[@class='lead-info__occupation']").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 326 {str(e)}")
            sleep(5)

    # get city
    city = ''

    try:
        city = browser.find_element(By.XPATH,
                                    "//div[text()='City']//following-sibling::div").get_attribute(
            'textContent')
    except:

        try:
            city = browser.find_element(By.XPATH,
                                        "//div[text()='Location']//following-sibling::div").get_attribute(
                'textContent')
        except:
            pass

    # get position
    while True:
        try:
            position = browser.find_element(By.XPATH,
                                            "//div[text()='Position']//following-sibling::div").get_attribute(
                'textContent')
            break
        except Exception as e:
            print(f"error line 352 {str(e)}")
            sleep(5)

    # get linkedIN link
    while True:
        try:
            linkedin = browser.find_element(By.XPATH,
                                            "//a[@title='Linkedin account']").get_attribute('href')
            break
        except Exception as e:
            print(f"error line 352 {str(e)}")
            sleep(5)

    date_now = datetime.datetime.now().strftime('%m-%d-%Y %H:%M')

    scraped_data = [[name, account_name, msg_text, company, is_big_law, title, position, email, city, linkedin, assign_to, date_now]]

    return scraped_data