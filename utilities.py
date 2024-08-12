def display_title(title):
    title = "|".join(title.upper())
    print(f"[{title}]".center(29))


def get_initials(name):
    initials = ""
    for name in name.upper().split():
        initials += name[0]
    if len(initials) <= 3:
        return initials
    else:
        return f"{initials[0]}{initials[-1]}"


