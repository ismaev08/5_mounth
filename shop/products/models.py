from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title}"