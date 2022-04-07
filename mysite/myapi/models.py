from django.db import models as m
class user(m.Model):
    name = m.CharField(max_length=60)
    bankID = m.CharField(max_length=12)
    dateCreation = m.DateField(auto_now=False,auto_now_add=True)
    balance = m.DecimalField(max_digits=19,decimal_places=2)
    birthday=m.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name


class bank(m.Model):
    name = m.CharField(max_length = 20)

    def __str__(self):
        return self.name