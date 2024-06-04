attendees = int(input("Enter number of attendees: "))  #correction was to specify a integer input
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if venue == "conference room":
   add_on = str(input("would you like to include a projector? "))
   if add_on == "yes":
    print("We will have a projector inlcuded with the conference room.") #expanded to add additonal facilities
if venue == "large hall":
     add_on = str(input("would you like to include and audio system "))
if add_on == "yes":
     print("an audio system will be provided")

veggie_options = input("would you like to include vegetarian options? ") #expanded in order to add catering options

if veggie_options == "yes":
    print("you should consider Veggie Delight Caterers")
else:
    print("you should consider Gourmet Meals Caterers")
    