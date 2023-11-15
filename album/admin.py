from django.contrib import admin
from album.models import Selection, Player, Aeropuerto, Vuelo, Pasajero

# Register your models here.
admin.site.register(Selection)
admin.site.register(Player)
admin.site.register(Aeropuerto)
admin.site.register(Vuelo)
admin.site.register(Pasajero)