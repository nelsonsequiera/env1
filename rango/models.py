from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique = True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    
    def __unicode__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        print 'slugging..'
        self.slug = slugify(self.name)
        super(category, self).save(*args, **kwargs)


class page(models.Model):
    category = models.ForeignKey(category)
    title = models.CharField(max_length = 200)
    url = models.URLField()
    views = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.title
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to = 'profile_images', blank = True)
    
    def __unicode__(self):
        return self.user.username
    
    
   