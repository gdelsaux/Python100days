states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

# print a state at index n
print(states_of_america[1])
# also work with negative number
print(states_of_america[-1]) # expect the last number in the list

# reassigned value
states_of_america[0] = states_of_america[0] + " Reassigned"
print(states_of_america)

# add a single item
states_of_america.append("added state")
print(states_of_america)

# add multiple items
states_of_america.extend(["added multiple 1", "added multiple 2"])
print(states_of_america)

# a list of list methods can be found here
# https://www.w3schools.com/python/python_ref_list.asp
