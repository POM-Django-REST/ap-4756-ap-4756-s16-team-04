from xml.dom import ValidationError
from django.core.validators import validate_email
from authentication.constants import MAX_EMAIL_CHARACTERS, MAX_NAME_CHARACTERS


def valid_bio_info(*args):
    for arg in args:

        if arg and len(arg) > MAX_NAME_CHARACTERS:
            raise ValidationError

    else:
        return True


def valid_email(email):
    try:
        validate_email(email)

        if len(email) > MAX_EMAIL_CHARACTERS:
            raise ValidationError
    
    except ValidationError:
        raise

    else:
        return True
