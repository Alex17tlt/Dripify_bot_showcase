import re

phrases = (
    'my cell is',
    'reach me at',
    'call me at',
    'mobile is',
    'my number is',
    'contact me on',
    'direct line is',
    'my digits',
    'Ring me at',
    'phone is',
    'get me at',
    'available at',
    'Dial me on',
    'ping me at',
    'reached at'
)

phone_number_regex = re.compile(r"""
    (?:                # Non-capturing group for the entire phone number
    \(?                # Optional opening parenthesis
    (\d{3})            # Area code (3 digits)
    \)?                # Optional closing parenthesis
    [-.\s]?            # Optional separator (dash, dot, or space)
    (\d{3})            # Exchange code (3 digits)
    [-.\s]?            # Optional separator (dash, dot, or space)
    (\d{4})            # Line number (4 digits)
    (?:                # Non-capturing group for extension (optional)
        \s?            # Optional space
        (?:ext|x|ext.) # Extension indicator
        \s?            # Optional space
        (\d{1,4})      # Extension number (1-4 digits)
    )?                 # End of optional extension group
    )                  # End of non-capturing group for the entire phone number
""", re.VERBOSE | re.IGNORECASE)

def is_phone_number_present(text):


    # check for phrases
    for i in phrases:

        if i.lower() in text.lower():
            print(f'\nPhone number PRESENT, do not reply')

            return True

    matches = phone_number_regex.findall(text)

    if len(matches) > 0:

        print(f'\nPhone number PRESENT, do not reply')

        return True
    else:
        return False