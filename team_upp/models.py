from django.db import models
from django.contrib.auth.models import User
from accounts.models import Extendeduser
# Create your models here.


class Teams(models.Model):
    category = models.CharField(max_length=100)
    relevant_url = models.URLField(default='Not Provided')
    pub_date = models.DateTimeField(null=True, blank=True)
    # image = models.ImageField(upload_to='images/')
    # icon = models.ImageField(upload_to='images/')
    short_description = models.TextField(
        default='Not Provided', max_length=200)
    description = models.TextField(default='Not Provided', max_length=2000)
    vacancy = models.IntegerField(default=1)
    logged_in_user = models.ForeignKey(Extendeduser, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class RecruitedTeammates(models.Model):
    teamup_advertisement = models.ForeignKey(Teams, on_delete=models.CASCADE,
                                             related_name='Tup_Advertisement')
    teammates = models.ForeignKey(Extendeduser, on_delete=models.CASCADE,
                                  related_name='teammates')


class ApplicationStatus(models.Model):
    logged_in_user = models.CharField(max_length=100, null=True)
    requester = models.CharField(max_length=100, null=True)
    teamup_advertisement = models.IntegerField(null=True)
    # TODO enum field to set values.
    status = models.CharField(max_length=2, default='NA', null=True)
    date = models.DateTimeField(null=True, blank=True)
    comments = models.CharField(max_length=1000, default='Not Provided')
    # TODO enum field to set values.
    signal = models.IntegerField(default=0, null=True)
