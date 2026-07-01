from django.db import models
from pgvector.django import VectorField

class Cliente(models.Model):

    SEGMENTO_CHOICES = [
        ('varejo', 'Varejo'),
        ('saude', 'Saúde'),
        ('transporte', 'Transporte'),
        ('industria', 'Indústria'),
    ]

    nome_cliente = models.CharField(max_length=255)
    segmento = models.CharField(max_length=100, choices=SEGMENTO_CHOICES, default='varejo')

    def __str__(self):
        return self.nome


class Projeto(models.Model):

    STATUS_CHOICES = [
        ('finalizado', 'Finalizado'),
        ('andamento', 'Em andamento'),
        ('planejamento', 'Planejamento'),
        ('pausado', 'Pausado'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='projetos'
    )
    nome_projeto = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='finalizado')

    def __str__(self):
        return f"{self.nome_projeto} - {self.cliente.nome}"
    
class Contrato(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='contratos'
    )
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='contratos'
    )
    conteudo = models.FileField(upload_to='documentos/')
    conteudo_texto = models.TextField()
    valor = models.DecimalField(decimal_places=2)

class Chunk(models.Model):

    contrato = models.ForeignKey(
        Contrato,
        on_delete=models.CASCADE,
        related_name='chunks'
    )
    conteudo = models.TextField()
    embedding = VectorField(dimensions=1536)
