from django.db import models


class Academy(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Academy'
        verbose_name_plural = 'Academys'


class Manager(models.Model):
    name = models.CharField(max_length=50)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


class Mentor(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentor'


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    # academy = models.OneToOneField(Academy, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
