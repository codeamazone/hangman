def check_email(string):
    if ' ' in string:
        return False
    elif '@' in string and '.' in string:
        position1 = string.index('@')
        position2 = string.rfind('.')
        return position2 > position1 + 1
    else:
        return False
