from django.contrib import admin
from .models import UserPost
from .models import User
from .models import Lawyer
from .models import Ngo
from .models import Therapist
from .models import Opportunity

admin.site.register(User)
admin.site.register(UserPost)
admin.site.register(Lawyer)
admin.site.register(Ngo)
admin.site.register(Therapist)
admin.site.register(Opportunity)