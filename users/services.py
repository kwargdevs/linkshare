from django import forms

def clean_password(password: str) -> str:
    symbols = "@#_~[]{}()$&?%/"
    
    # MinimumLengthValidator
    if len(password) < 10:
        raise forms.ValidationError(
            "Password is too short. Requires a minimum of 10 characters")

    # CommonPasswordValidator
    if password.isdigit() or password.isalpha():
        raise forms.ValidationError("Password is too common.")

    # NoSymbolValidator
    if not any([sym in symbols for sym in password]):
        raise forms.ValidationError(
            f"Password should contain any of {symbols}")

    return password
