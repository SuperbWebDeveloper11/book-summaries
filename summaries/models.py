from django.db import models
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager



class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True
        ordering = ('created', )


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
                     
    def __str__(self):
        return self.name
                     

class Summary(TimeStampedModel):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='summaries')
    body = models.TextField(blank=True)
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='summaries')

    def get_absolute_url(self):
        return reverse('summaries:summary_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
                     


