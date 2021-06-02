import phonenumbers
number = input("Enter a phone number: ")
country_code = input("Enter country Code with + : ")
number = country_code + number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
from phonenumbers import carrier
carrier_service = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(carrier_service, "en"))