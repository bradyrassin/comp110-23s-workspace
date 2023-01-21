"""Knock Knock joke with conditionals"""

inter_cow: str = input("Do you want to hear a knock knock joke? ")


if (inter_cow == "yes"):
    print("Knock knock")
    print("... who's there?")
    print("interrupting cow.")
    print("... interrupting cow wh--")
    print("MOO!!!")
else:
    print("Wow guess someone isn't very fun :( ")
    if (inter_cow == "you're not funny"):
        print("Screw you")