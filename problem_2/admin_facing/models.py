from django.db import models

# App model for storing app details
class App(models.Model):
    app_name = models.CharField(max_length=100)
    app_image = models.ImageField(upload_to='app_images', null=True, blank=True)
    app_link = models.CharField(max_length=200)
    categories = [('entertainment', 'Entertainment'), ('games', 'Games'), ('tools', 'Tools')]
    category = models.CharField(max_length=100, choices=categories)
    sub_categories = [('social_media', 'Social Media'), ('archery','Archery'),('action', 'Action'), ('video_player','Video Player'), ('image_editor', 'Image Editor')]
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.app_name