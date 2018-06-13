from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from .validations import validate_person_email_or_contact

# Create your models here.
class LostAndFound(models.Model):

    lost_or_found_choice_field = (
                        ('lost', 'Lost'),
                        ('found', 'Found'),
    )
    status_choice_field        = (
                        ('pending', 'Pending'),
                        ('solved', 'Solved'),
    )
    lost_or_found                       = models.CharField(max_length = 10 ,choices = lost_or_found_choice_field)
    title                               = models.CharField(max_length = 50, help_text = 'e.g Lost mobile at 210 lab.')
    description                         = models.TextField(max_length = 300)
    slug                                = models.SlugField(blank = True) # editable = False, error_message = {}, help_text = ''
    image                               = models.ImageField(null = True, blank = True)
    contact_person_name                 = models.CharField(max_length = 20)
    contact_person_mobile_or_email      = models.CharField(max_length = 30, validators= [validate_person_email_or_contact])
    date_found_or_lost                  = models.DateField(verbose_name = 'lost or found date ', default= timezone.now)
    date_published                      = models.DateField(verbose_name = 'published date', default= timezone.now)
    status                              = models.CharField(max_length = 10, choices = status_choice_field, default = 'pending') 
    date_solved                         = models.DateField(verbose_name = 'solved date', blank=True, null=True)
    author                              = models.CharField(max_length=50, blank=True, null=True)
    author_email                        = models.CharField( max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(LostAndFound, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return self.title
    
    def get_queryset(self):
        queryset = super(LostAndFound, self).get_queryset().order_by('-id')
        return queryset

    
    