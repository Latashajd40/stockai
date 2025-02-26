def fake_predict(user_age):
    if user_age > 10:
        prediction = "survive (over ten)"
    else:
        prediction = "Super survive (under ten)"
    return prediction