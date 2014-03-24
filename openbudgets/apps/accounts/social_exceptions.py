from social_auth.exceptions import SocialAuthBaseException
from django.utils.translation import ugettext as _


class NonIdenticalEmailAddress(SocialAuthBaseException):
    def __unicode__(self):
        return _(u'Identical email error: {message}').format(message=self.message)
