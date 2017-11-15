from django.db import models

class Contact(models.Model):
    owner = models.ForeignKey('auth.User')
    FirstName = models.CharField(max_length=30, blank=False)
    LastName = models.CharField(max_length=30, blank=False)
    Email = models.EmailField(max_length=60, blank=True)

    def __str__(self):
        return self.LastName + ", " + self.FirstName