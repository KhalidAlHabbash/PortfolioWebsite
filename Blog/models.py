from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body_text = models.TextField(blank=True)
    blog_image = models.ImageField(upload_to="images/")

    def summary(self):
        if len(self.body_text)>200:
            return(self.body_text[0:100] + "...")
        else: return(self.body_text)

    def __str__(self):
        return (self.title)




