def format_name(firstname, lastname):
    """ Format the fullname of the person """

    return f"{firstname} {lastname}"

def format_birthdate(day, month, year):
    """ Format the birthdate of the person """

    return f"{month}/{day}/{year}"


firstname, lastname = "John", "Doe"
day, month, year = "01", "01", "2005"

print(f"{format_name(firstname, lastname)}")
print(f"Born on {format_birthdate(day, month, year)}")

