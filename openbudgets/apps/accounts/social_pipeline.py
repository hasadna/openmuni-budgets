from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.utils.translation import ugettext
from social_auth.models import UserSocialAuth
from .models import Account
from social_auth.exceptions import AuthException
from social_exceptions import NonIdenticalEmailAddress


def associate_by_email(details, user=None, *args, **kwargs):
    """Return user entry with same email address as one returned on details."""
    email = details.get('email', None)

    if user and user.email == email:
        return None
    elif not email or (user and user.email != email):
        msg = ugettext('Social email address and account email ' +
                       'address must be idnetical')
        raise NonIdenticalEmailAddress(msg)
    if email:
        # Try to associate accounts registered with the same email address,
        # only if it's a single object. AuthException is raised if multiple
        # objects are returned.
        try:
            return {'user': UserSocialAuth.get_user_by_email(email=email)}
        except MultipleObjectsReturned:
            raise AuthException(kwargs['backend'], 'Not unique email address.')
        except ObjectDoesNotExist:
            pass


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
        'user': UserSocialAuth.create_user(username=username, email=email,
                                           first_name=first_name,
                                           last_name=last_name,
                                           password=password),
        'original_email': original_email,
        'is_new': True
    }
