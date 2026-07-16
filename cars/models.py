from django.db import models

# onde é definido o nome da tabela e campos (colunas)
# dentro de django.db tem um módulo de nome 'models' com arquivo __init__.py, do qual a classe Car herda de models.Model

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):    # o nome da classe é o nome da tabela no banco
    id = models.AutoField(primary_key=True)     # chave única do tipo AutoField - autoincremental
    model = models.CharField(max_length=200)    # tipo CharField - string, outros parâmetros possíveis: blank=True, null=True
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # <-- ajuste feito aqui para referenciar outro model criado (ou tabela no banco de dados)
    factory_year = models.IntegerField(blank=True, null=True)   # tipo IntegerField
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self): # <-- altera como um objeto da classe (instância) é exibido
        return self.model