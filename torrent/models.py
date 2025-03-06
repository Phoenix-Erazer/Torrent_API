from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Torrent(models.Model):
    LANGUAGE_CHOICES = [
        ("English", "Английский"),
        ("Russian", "Русский"),
        ("Ukrainian", "Украинский"),
    ]
    CATEGORY_CHOICES = [
        ("Games", "Игры"),
        ("Movies", "Фильмы"),
        ("TV_show", "Сериалы")
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    year_of_issue = models.DateField(null=False, blank=False)
    genre = models.ManyToManyField(Genre, related_name="torrents")
    game_developer = models.CharField(max_length=63)
    interface_language = models.CharField(
        max_length=10, choices=LANGUAGE_CHOICES,
        default="Russian"
    )
    system_requirements = models.TextField()
    description = models.TextField()
    background_picture = models.ImageField(null=True, blank=True) #needs finishing
    creation_date = models.DateField(auto_now_add=True)
    category =models.CharField(
        max_length=63,
        choices=CATEGORY_CHOICES,
        default="Movies"
    )
    hard_disk_space = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return f"{self.title} - {self.year_of_issue}, {self.genre}"
