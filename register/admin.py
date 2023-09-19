from django.contrib import admin
from .models import Team, Member, Hakaton


admin.site.register(Hakaton)
admin.site.register(Team)
admin.site.register(Member)


