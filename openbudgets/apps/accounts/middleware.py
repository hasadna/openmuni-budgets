from social_auth.middleware import SocialAuthExceptionMiddleware
from django.conf import settings


class OpenBudgetsSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	def get_redirect_uri(self, request, exception):
		return settings.LOGIN_URL