from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
		# configurações do admin
		list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
		search_fields = ('model',)
		
# agora é preciso indicar que a classe CarAdmin vai estar visível para o admin 
# através da função register e incluir os models Car e CarAdmin
admin.site.register(Car, CarAdmin) # parâmetros: (qual modelo?, quais configurações de admin?)