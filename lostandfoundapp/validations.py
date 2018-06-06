from django.core.exceptions import ValidationError

def validate_person_email_or_contact(value):
    if value.isnumeric():
        if not (len(value) == 10 and (value[0] == '9' or value[0] == '8' or value[0] == '7' )):
            raise ValidationError('Invalid mobile number') 
        return value  
    else:
        if '@' not in value:
            raise ValidationError('Invalid email address')
        return value