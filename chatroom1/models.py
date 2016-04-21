from django.db import models


class Message(models.Model):
    date = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    added = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {} -- {}".format(self.publisher, self.message, self.date)

    def __repr__(self):
        return str(self)
