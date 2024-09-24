import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number with + __: ")

try:
    phone = phonenumbers.parse(number)
    
    # Check Validation
    is_valid = phonenumbers.is_valid_number(phone)
    is_possible = phonenumbers.is_possible_number(phone)
    print(f"Valid: {is_valid}, Possible: {is_possible}")
    
    # Check for its type
    numbers_type = phonenumbers.number_type(phone)
    
    if numbers_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f"The number {phone} is a mobile number")
    elif numbers_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f"The number {phone} is a landline number")
    elif numbers_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
        print(f"The number {phone} could be either a landline or a mobile number")
    elif numbers_type == phonenumbers.PhoneNumberType.TOLL_FREE:
        print(f"The number {phone} is a toll-free number")
    elif numbers_type == phonenumbers.PhoneNumberType.VOIP:
        print(f"The number {phone} is a VOIP number")
    elif numbers_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
        print(f"The number {phone} is a premium-rate number")
    else:
        print(f"The number {phone} is of another type or not recognized")
    
    # Fetch additional details
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.description_for_number(phone, "en")
    
    print(f"Time Zone: {time}")
    print(f"Carrier: {car}")
    print(f"Region: {reg}")

except phonenumbers.NumberParseException as e:
    print(f"Error: {str(e)}")

