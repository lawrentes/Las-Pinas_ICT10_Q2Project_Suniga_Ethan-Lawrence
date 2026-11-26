from pyscript import document


def candidate_checker(e):
    # names of everyone allowed in the club (all lowercase)
    club_members = [
        "gible grachenheight", "danji spluffins", "ichentu nikkolas",
        "vurian willion", "kaytei mallador", "grakbet4 gh4ruiscili",
        "plaginon destructor", "cadence volition"
    ]

    # get what the user typed in the first name and last name boxes
    f_name = document.getElementById('fname').value
    l_name = document.getElementById('lname').value

    # join the two names with one space and remove extra spaces around them
    candidate = f"{f_name.strip()} {l_name.strip()}"

    # check if the name is in the list, using lowercase so capitals
    # don't matter
    is_member = candidate.lower() in club_members

    # pick the message to show depending on the result
    if is_member:
        message = (
            f"Congratulations, {candidate} individual! You are part of the "
            "Xarian Aviation Club. Now please drive a rocket to Splork, "
            "we need more Yuogliptonium-246."
        )
    else:
        message = (
            f"Sorry {candidate}, your name is not on the Xarian Aviation "
            "Club list. Please leave now."
        )

    # show the message on the page
    document.getElementById('result').innerHTML = message
