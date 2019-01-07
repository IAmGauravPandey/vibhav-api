from django.contrib import admin
from .models import UserProfile,Event,UserToken,Registration,EventRules
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    
    list_display=('event','team_name','user','token')
    
    def get_queryset(self,request):
        queryset=super(RegistrationAdmin,self).get_queryset(request)
        queryset=queryset.order_by('event','team_name','user')
        return queryset

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','branch','name','coins','phone')
    
    def get_queryset(self,request):
        queryset=super(UserProfileAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-coins','-user','-branch','-phone')
        return queryset

class EventAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(UserToken)
admin.site.register(EventRules)
admin.site.site_header='Admin'