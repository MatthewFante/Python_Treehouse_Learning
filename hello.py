first_name = input("what is your first name?  ")

print("Hello,", first_name)

if first_name == "Matthew":
    print(first_name, "is learning python")
elif first_name.lower() == "booty":
    print("You sound thick, {}".format(first_name))    
else: 
    # This is just in case we have a younger user who cannot yet read
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow! You're {}! If you're confident with your reading already...".format(age))

    print("You should totally learn python {}!".format(first_name))    

print("Have a great day, {}".format(first_name))
