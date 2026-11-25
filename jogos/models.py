from django.db import models

# Create your models here.

class Desenvolvedora(models.Model):
    nome = models.CharField("Nome", max_length=120, unique=True)
    pais = models.CharField("País", max_length=80, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Desenvolvedora"
        verbose_name_plural = "Desenvolvedoras"

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField("Nome", max_length=80, unique=True)
    fabricante = models.CharField("Fabricante", max_length=80, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField("Nome do jogo", max_length=200)
    ano_lancamento = models.PositiveIntegerField("Ano de lançamento", null=True, blank=True)
    desenvolvedora = models.ForeignKey(
        Desenvolvedora,
        on_delete=models.CASCADE,
        related_name="jogos",
        verbose_name="Desenvolvedora",
    )
    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name="jogos",
        verbose_name="Plataforma",
    )

    class Meta:
        ordering = ["nome"]
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"

    def __str__(self):
        return self.nome