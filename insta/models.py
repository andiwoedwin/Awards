from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from PIL import Image

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.CharField(max_length=50, blank=True)

   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



# class Review(models.Model):
#     ratings = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)
    
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
#     design = models.IntegerField(choices=ratings, default=0)
#     usability = models.IntegerField(choices=ratings, default=0)
#     creativity = models.IntegerField(choices=ratings, default=0)
#     content =  models.IntegerField(choices=ratings, default=0)
#     overall_score = models.IntegerField(blank=True, default=0)

#     def save_rate(self):
#             self.save()

#     def delete_rate(self):
#         self.delete()

#     def get_absolute_url(self):
#         return reverse('index')