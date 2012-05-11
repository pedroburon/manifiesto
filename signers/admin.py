from django.contrib import admin

from signers.models import Signer


class SignerAdmin(admin.ModelAdmin):
    list_display = ['user_first_name', 'user_last_name', 'country']
    search_fields = ['user__first_name']
    list_filter = ['subscribed']

    def user_first_name(self, instance):
        return instance.user.first_name

    def user_last_name(self, instance):
        return instance.user.last_name


admin.site.register(Signer, SignerAdmin)
