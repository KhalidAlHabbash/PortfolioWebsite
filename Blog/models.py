from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body_text = models.TextField(blank=True)
    blog_image = models.ImageField(upload_to="images/")