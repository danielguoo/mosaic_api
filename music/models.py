from django.db import models


class Album(models.Model):
    released = models.IntegerField()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=20, default='', blank=True)
    cover_art = models.CharField(max_length=50)
    spotify_URL = models.CharField(max_length=100)

    class Meta:
        ordering = ('released',)

    def __str__(self):
        return self.title


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    synopsis = models.CharField(max_length=150)
    review_text = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'auth.User', related_name='reviews', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', 'album',)
