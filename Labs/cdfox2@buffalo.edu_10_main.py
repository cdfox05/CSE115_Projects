import math

def abv_simple(pre, post):
    abv = (pre-post)*131.25
    return round(abv,2)


def abv_precise(pre, post):
    abv = (76.08*(pre-post)/(1.775-pre))*(post/.794)
    return round(abv,2)


def canadianize(str):
    str = str.replace("er ","re ")
    str = str.replace("or", "our")
    return str


def absolute_difference(pre, post):
    ab = abv_simple(pre,post)-abv_precise(pre,post)
    ab = abs(ab)
    ab = round(ab,2)
    return ab

