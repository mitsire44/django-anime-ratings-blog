from django.db import models

# Create your models here.
class Review(models.Model):
    image = models.ImageField(upload_to='reviews/images/')
    yalscore = models.IntegerField(blank=True)
    title = models.CharField(max_length=75)
    desc = models.TextField(max_length=2000, blank=True)
    userscore = models.IntegerField(blank=True, default=0)
    url = models.URLField(blank=True)
    votes = models.IntegerField(default=0)
    totalscore = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.CharField(max_length=20)
    review = models.TextField(max_length=500)
    anime = models.ForeignKey(Review, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, blank=True)

# class Score(models.Model):
#     # scores = [
#     #     ('0', '0'),
#     #     ('20', '20'),
#     #     ('40', '40'),
#     #     ('60', '60'),
#     #     ('80', '80'),
#     #     ('100', '100')
#     # ]
#     anime = models.ForeignKey(Review, on_delete=models.CASCADE)
#     score = models.IntegerField(blank=True, default=0)
#     # score = models.CharField(max_length=10,
#     #     choices=scores,
#     #     default='0',
#     # )
#     votes = models.IntegerField(default=0)

