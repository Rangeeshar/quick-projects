# Shorten or enlarge a URl
# Sample -> https://google.com -> https://shortened.com/sadjuhasjkdghasdgh
import hashlib

GLOBAL_MOCK_DICT = {}
GLOBAL_COUNT = 0


def shorten_url(url):
    """
    Shorten the URL
    """
    global GLOBAL_COUNT
    hashed_data = "#SHT_{}".format(GLOBAL_COUNT)
    GLOBAL_MOCK_DICT[hashed_data] = url
    template_url = "https://shortened.com/{}".format(hashed_data)
    GLOBAL_COUNT += 1
    return template_url


def fetch_actual_url(url):
    """
    Fetch actual URL
    """
    return GLOBAL_MOCK_DICT[url.split("/")[-1]]


while 1:
    user_input = input("What action Do you want to do 1. Shorten a URL \n2. Get Actual URL.\n 3. Exit\n")
    if int(user_input) == 1:
        url_entered = input("Enter the URL you want to short: ")
        print(shorten_url(url_entered))
    elif int(user_input) == 2:
        url_entered = input("Enter the shortened URL: ")
        print(fetch_actual_url(url_entered))
    elif int(user_input) == 3:
        break
    else:
        print("not valid input..")
