from django.contrib import admin
# from .models import Candidate, Job, Company
from import_export import resources, fields, widgets
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget

from .models import Company, Job


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['co_name', 'co_city']


admin.site.register(Company, CompanyAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ['job_profile', 'job_city']


admin.site.register(Job, JobAdmin)

# class CandidateAdmin (admin.ModelAdmin):
#     list_display = ['name','city']
# admin.site.register(Candidate,CandidateAdmin)

# Register your models here.

from .models import Profiles


from import_export.admin import ImportExportModelAdmin

class ProfilesResource(resources.ModelResource):
    company=fields.Field(column_name='company', attribute='company',widget=widgets.ForeignKeyWidget(Company,'co_name'))

    class Meta:
        model = Profiles
        report_skipped = True
        exclude = ('id')
        import_id_fields =('name', 'email', 'address', 'phone', 'profile','company',)

class ProfilesAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    resource_class = ProfilesResource
admin.site.register(Profiles,ProfilesAdmin)
