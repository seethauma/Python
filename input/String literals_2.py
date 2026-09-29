from email import message

name="Muruga"

print(name.lower())
print(name.upper())
print(name.capitalize()) # First Letter in caps

mobile="9965525418"
masked=mobile[:2] + "******" + mobile[-2:]# indicates first 2 numbers and last two numbers(-2)
print(masked)



song="shape OF you"
artist="GOWTHAM"
#to format first letter alone to cap
formatted=f"{song.title()} {artist.title()}"
print(formatted)


location="Chicago"
fixed_location=location.replace("Chicago","Buffalo Grove")
print(fixed_location)

display_message="your order is ready id is:B12345.Please keep it safe"
#here 1=> : is the delimiter so [1] before : is [0] and after : is [1]
#     2=> then . is the delimiter so [0] is B12345 and after . is [1]
#     here we need to get the id so both extra sentence before and after id
get_id_only=display_message.split(":")[1].split(".")[0].strip()

print(get_id_only)
print(display_message)