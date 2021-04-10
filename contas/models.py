from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=140) 
    dt_criacao = models.DateTimeField(auto_now_add=True) #Guarda a data automaticamente
    
    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.descricao
