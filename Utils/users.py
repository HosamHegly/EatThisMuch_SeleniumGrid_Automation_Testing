from operator import itemgetter

# we can store test data in this module like users
valid_users = [
    {"name": "Hosam", "email": "hosamhegly@gmail.com", "password": "weponsofshit123"},

]

invalid_users = [
    {"name": "invalid", "email": "invalidUser@test.com", "password": "qwert1235"},
    {"name": "Saeed", "email": "saeedesawi@test.com", "password": "afj322rfe"},

]


def get_valid_user(name):
    try:
        return next(user for user in valid_users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


def get_invalid_user(name):
    try:
        return next(user for user in invalid_users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


def get_all_valid_users():
    return valid_users


def get_all_invalid_users():
    return invalid_users
