from django.db import models

# Create your models here.
class Questao(models.Model):
    texto_da_questão = models.CharField(max_length=200)
    data_de_publicacao = models.DateTimeField(verbose_name = u'Data de Publicacão')

    def __str__(self):
        return self.texto_da_questão

class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete = models.CASCADE)
    testo_da_alternativa = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.testo_da_alternativa