from django.core.exceptions import ValidationError

class CustomPasswordValidator():
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(f'Password must contain at least {self.min_length} digit.')
        if not any (char.isupper() for char in password):
            raise ValidationError(f'Password must contain at least {self.min_length} capital letter.')
        if any(char in special_characters for char in password):
            raise ValidationError(f'Password cannot contain a special character.')
        
    def get_help_text(self):
        return ""