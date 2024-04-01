from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_date',)

    def save(self, *args, **kwargs):
        if not self.subject:
            self.subject = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email



