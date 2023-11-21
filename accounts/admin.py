from django.contrib import admin
from .models import Teacher, Subject, Class, Student, Grade

class GradeInline(admin.TabularInline):
    model= Grade
    extra= 1

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name','subject_taught', 'date_of_join')

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('id')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'full_marks', 'pass_marks')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'class_teacher')
    filter_horizontal = ('subjects',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'enrolled_class', 'date_of_birth')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'marks_obtained')

# Register your models
# admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(Subject, SubjectAdmin)
# admin.site.register(Class, ClassAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Grade, GradeAdmin)