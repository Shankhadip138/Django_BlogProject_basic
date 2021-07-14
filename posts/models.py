from django.db import models

# Create your models here.

class People (models.Model):
    Name = models.CharField(max_length=60)
    Email= models.EmailField(max_length = 254,unique = True)
    def __str__(self):
        return self.Name


class BlogContent (models.Model):
    Blogg=models.CharField(max_length=300)
    pub_date = models.DateTimeField('date Published')
    pep = models.ForeignKey(People,on_delete=models.CASCADE,related_name='Person_obj')
    def __str__(self):
        return self.Blogg
class Comments(models.Model):
    Comm= models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Comment Date')
    commenter = models.CharField(max_length=60, default = 'Anonnymous')
    blg= models.ForeignKey(BlogContent,on_delete=models.CASCADE,related_name='Commentss')
    def __str__(self):
        return self.Comm
