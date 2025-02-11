from django.contrib import admin
from .models import (
    Slider, WhoWe, Advantage, Settings, 
    Stages_of_work, Carts_for_stages_of_work, Text_gallery, Gallery)

admin.site.register(Settings)
admin.site.register(Slider)
admin.site.register(Advantage)
admin.site.register(WhoWe)
admin.site.register(Stages_of_work)
admin.site.register(Carts_for_stages_of_work)
admin.site.register(Text_gallery)
admin.site.register(Gallery)
