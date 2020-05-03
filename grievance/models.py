from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

Student = get_user_model()

class Grievance(models.Model):

        user = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='grievances')
        title= models.CharField(max_length=50)
        description=models.TextField()
        against = models.CharField(max_length=30)
        create_Date=models.DateTimeField(auto_now=True)
        post_Date=models.DateTimeField(blank=True,null=True)
        status = models.PositiveIntegerField(default=0)
        resolved=models.BooleanField(default=False)

        def save(self,*args,**kwargs):
            super().save(*args,**kwargs)

        def post(self):
            self.post = timezone.now()
            self.save()

        def get_absolute_url(self):
             return  reverse(
                "grievance:single",
                kwargs={
                    "username": self.user.username,
                    "pk": self.pk
                }
        )

        def stat_update(self):
            self.status+=1
            if(self.status==5):
                self.resolved=True
            self.save()
        
        def __str__(self):
            return self.title

        class Meta:
            ordering = ["-create_Date"]
            unique_together= ["user","title"]