from django.contrib import admin
from .models import Category , Post , Feedback , Contact
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Feedback)
admin.site.register(Contact)
