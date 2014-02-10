from social_auth.exceptions import SocialAuthBaseException
from django.utils.translation import ugettext


class NonIdenticalEmailAddress(SocialAuthBaseException):
    def __unicode__(self):
        return ugettext(u'Identical email error: %(message)s' % {'message':
                                                                 self.message})
