from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True) #blank True - Não obriga que o campo seja preenchido, Blank False - Obriga que seja preenchido. Null True - Permite que o valor salve como nulo. Além disso, nem sempre é necessário definir os dois quando quiser um campo opcional. Valores de string, como a CharFieldou a TextFielddevem ser armazenados em uma string vazia, portanto, você deve usar apenas blank=True. No seu caso, sem obrigatoriedade, IntegerFieldvocê deve usar os dois blanke null 

    note = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username