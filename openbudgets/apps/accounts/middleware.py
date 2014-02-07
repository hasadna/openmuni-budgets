from social_auth.middleware import SocialAuthExceptionMiddleware
from django.contrib import messages
from social_auth.exceptions import *
from django.utils.translation import ugettext as _
from django.conf import settings


class OpenBudgetsSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	def get_redirect_uri(self, request, exception):
		return settings.LOGIN_URL