# django own imports
from django.contrib import admin
# users own imports
from users.models import VerificationCodeModel

admin.site.register(VerificationCodeModel)
