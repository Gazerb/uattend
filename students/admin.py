from django.contrib import admin

from .models import Students, Grades, Attendance

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'name',
        'university',
        'major',
    )

    ordering = ('student_id',)

class GradesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'subject',
        'grade_score',
    )

class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'subject',
        'attendance_score',
    )

# Register your models here.
admin.site.register(Students, StudentAdmin)
admin.site.register(Grades, GradesAdmin)
admin.site.register(Attendance, AttendanceAdmin)