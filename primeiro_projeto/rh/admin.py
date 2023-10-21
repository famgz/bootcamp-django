from django.contrib import admin
from rh.models import Pessoa, Contato

# Register your models here.


class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'apelido', 'cpf']  # add columns fields on /admin/rh/pessoa/
    search_fields = ['nome', 'apelido', 'cpf']
    inlines = [ContatoInline]


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'telefone', 'email', 'tipo']
    list_filter = ['pessoa', 'tipo']
    search_fields = ['telefone', 'email', 'pessoa__nome']
