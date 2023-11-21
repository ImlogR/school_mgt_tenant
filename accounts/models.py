from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    full_marks= models.IntegerField(blank=True, null=True)
    pass_marks= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_taught = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    enrolled_class= models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    # grade = models.DecimalField(max_digits=5, decimal_places=2)
