import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobilelo = input("Enter Mobile Number with Country codes=")
mobilelo = phonenumbers.parse(mobilelo)

# get timezone a phone number 8 
print(timezone.time_zones_for_number(mobilelo))



# Getting carrier of a phone number 11 
print(carrier.name_for_number (mobilelo, "en"))

# Getting region information 14 
print (geocoder.description_for_number(mobilelo, "en"))

# Validating a phone number 17 
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobilelo))

 # Checking possibility of a number 28 
print("Checking possibility of Number:", phonenumbers.is_possible_number(mobilelo))