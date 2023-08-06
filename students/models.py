from django.db import models

# Create your models here.

class Students(models.Model):

    class Meta:
        verbose_name_plural = 'Students'


    name = models.CharField(max_length=254)
    university = models.CharField(max_length=254)
    major = models.CharField(max_length=254)
    student_id = models.IntegerField()

    def __str__(self):
        return self.name


class Grades(models.Model):

    class Meta:
        verbose_name_plural = 'Student Grades'

    name = models.ForeignKey('students', null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=254)
    grade_score = models.IntegerField()

    def __str__(self):
        return self.subject


class Attendance(models.Model):

    class Meta:
        verbose_name_plural = 'Attendance Scores'


    name = models.ForeignKey('students', null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey('grades', null=True, blank=True, on_delete=models.SET_NULL)
    attendance_score = models.CharField(max_length=3)

    def __str__(self):
        return self.attendance_score