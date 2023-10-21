from django.db import models

# Create your models here.

'''
Pessoa
-nome
-data de nascimento
-apelido
-cpf

Contato
-tipo
    pessoal
    trabalho
-telefone
-email
'''


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    data_nascimento = models.DateField()
    apelido = models.CharField(max_length=32, null=True)  # null=True -> optional field
    cpf = models.CharField(max_length=14)

    # change entry representation on /admin/rh/pessoa/
    def __str__(self):
        return self.nome


class Contato(models.Model):
    TIPO_CHOICES = (
        ('pessoal', 'Contato Pessoal'),
        ('trabalho', 'Contato de trabalho')
    )

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=32, choices=TIPO_CHOICES)
    telefone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'PESSOA: {self.pessoa} - TELEFONE: {self.telefone} - EMAIL: {self.email}'
