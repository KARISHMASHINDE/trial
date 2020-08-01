from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	    """
	    Author : Karishma Shinde
	    Use : tags
	    """
	    word        = models.CharField(max_length=35)
	    slug        = models.CharField(max_length=250)
	    created_at  = models.DateTimeField(auto_now=True)
	

	    def __unicode__(self):
	        return self.word
	

	    def __str__(self):
	        return self.word


class Posts(models.Model):
    Title = models.CharField(max_length=100)
    Body = models.TextField() 
    Date_posted = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    Author_id = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    Image = models.ImageField(upload_to='images/',null=True,blank=True)
    claps = models.ManyToManyField(User,blank = True, related_name="claps")
    Tags = models.ManyToManyField(Tag,blank=True, related_name="Tags")
    slug = models.SlugField()



    def __str__(self):
        return str(self.Title)

    
    def get_api_claps_url(self):
        return reverse("BlogPost:claps-api-toggle", kwargs={"slug": self.slug})

    @property
    def total_claps(self):
        return self.claps.all().count()
    
    
    
