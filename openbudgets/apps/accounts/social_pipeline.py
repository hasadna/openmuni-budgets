from social_auth.models import UserSocialAuth
from .models import Account

def create_user(backend, details, response, uid, username, user=None, *args,
                **kwargs):
    """Create user. Depends on get_username pipeline."""
    if user:
        return {'user': user}
    if not username:
        return None

    # Avoid hitting field max length
    email = details.get('email')
    original_email = None
    if email and UserSocialAuth.email_max_length() < len(email):
        original_email = email
        email = ''
    first_name = details.get('first_name') or 'John'
    last_name = details.get('last_name') or 'Doe'
    password = Account.objects.make_random_password()

    return {
        'user': UserSocialAuth.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password),
        'original_email': original_email,
        'is_new': True
    }