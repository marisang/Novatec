from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    segmento = models.CharField(max_length=100)
    data_entrada = models.DateField()
    def __str__(self):
        return self.nome

class Projeto(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="projetos"
    )
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    data_inicio = models.DateField()
    data_fim = models.DateField(
        null=True,
        blank=True
    )
    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="pagamentos"
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    data_pagamento = models.DateField()
    status = models.CharField(
        max_length=50
    )

class Contrato(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="contratos"
    )
    arquivo_pdf = models.TextField()
    data_assinatura = models.DateField()
    class ChatHistory(models.Model):
        session_id = models.CharField(
        max_length=255
    )
    role = models.CharField(
        max_length=20
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )