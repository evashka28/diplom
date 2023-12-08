from django.db import models

from tenant_users.tenants.models import UserProfile

_NameFieldLength = 64


class TenantUser(UserProfile):
    """Simple user model definition for testing."""

    name = models.CharField(max_length=_NameFieldLength, blank=True)


'''
class Doctor(models.Model):

    #doc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    def __str__(self):
        return self.name



class Schedule(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"name")
    room = models.IntegerField(verbose_name=u"room")
    mon = models.CharField(max_length=255)
    tue = models.CharField(max_length=255)
    wed = models.CharField(max_length=255)
    thu = models.CharField(max_length=255)
    fri = models.CharField(max_length=255)
    sat = models.CharField(max_length=255)
    sun = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Patient(models.Model):
    #pat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=u"name", blank=True)
    surname = models.CharField(max_length=255, verbose_name=u"surname", blank=True)
    phone_number = models.CharField(max_length=255, verbose_name=u"mobile", null=True, blank=True)
    birth = models.DateField(max_length=255, verbose_name=u"bithday", blank=True, null=True)
    user_id = models.OneToOneField(TenantUser, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.name

    # def getbyuserid(id):
    #     return self.name


class MedicalCard(models.Model):
    #id = models.AutoField(primary_key=True)
    app_date = models.DateTimeField(max_length=255, verbose_name=u"date")
    diagnosis = models.CharField(max_length=255, verbose_name=u"diagnosis")
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)


    def __str__(self):
        return self.diagnosis


class Appointment(models.Model):
    #id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.DateTimeField()



'''
