def determine(me=False, wife=True):
    if me and wife:
        return 'My wife is correct'
    elif not me and wife:
        return 'My wife is correct'
    elif me and not wife:
        return 'My wife is correct'
    elif not me and not wife:
        return 'I am incorrect'