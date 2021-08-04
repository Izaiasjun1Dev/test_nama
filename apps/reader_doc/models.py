import os
import sys
from django.db import models

"""
Comprador	
Descrição	
Preço Unitário	
Quantidade	
Endereço	
Fornecedor
"""

def upload_to_doc(filename):
    pass

class DocVendas(models.Model):
    file = models.FileField(upload_to=None, max_length=100)

class InfoVendas(models.Model):
    comprador = models.CharField(max_length=80)
    descricao = models.CharField(max_length=100)
    preco_unitario = models.CharField(max_length=15)
    qtd = models.CharField(max_length=10)
    fornecedor = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"comprador: {self.comprador}, qtd: {self.qtd}"
