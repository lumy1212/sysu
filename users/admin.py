from django.contrib import admin

from users.models import Person

class PersonAdmin(admin.ModelAdmin):
    Person.objects.order_by("id")
    list_display = ('id','name','student_id','grade','major','email')

admin.site.register(Person,PersonAdmin)