from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    segmento = models.CharField(max_length=100)
    data_entrada = models.DateField(null=True, blank=True)
    @property  #faz com que o valor total seja uma soma automática dos valores de todos os preojetos do cliente, ***não consegui testar
    def valor_total_cliente(self):
        return self.projetos.aggregate(
            total=Sum("valor_projeto")
        )["total"] or 0

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="projetos"
    )
    nome_projeto = models.CharField(max_length=255)
    status_projeto = models.CharField(max_length=50)
    valor_total_projeto= models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    def __str__(self):
        return self.nome_projeto
