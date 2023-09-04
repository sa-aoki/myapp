from django.contrib import admin
from .models import Project_info, Level, Wall_finish, Ceiling_finish, Floor_finish, Room
from import_export import resources
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export.formats import base_formats



class Project_infoAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_No', 'name', 'project_type')
    search_fields = ('project_No',)
    list_filter = ('name',)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class Wall_finishResource(resources.ModelResource):
    class Meta:
        model = Wall_finish 

class Wall_finishAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    base_formats.CSV.CONTENT_TYPE = 'text/csv; charset='
    resource_class = Wall_finishResource


class Ceiling_finishResource(resources.ModelResource):
    class Meta:
        model = Ceiling_finish 

class Ceiling_finishAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    base_formats.CSV.CONTENT_TYPE = 'text/csv; charset=CP932'
    resource_class = Ceiling_finishResource


class Floor_finishResource(resources.ModelResource):
    class Meta:
        model = Floor_finish 

class Floor_finishAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    base_formats.CSV.CONTENT_TYPE = 'text/csv; charset=CP932'
    resource_class = Floor_finishResource




#部屋
class RoomResource(resources.ModelResource):
    class Meta:
        model = Room 
        import_id_fields = ('IfcGUID',) 
        fields=('project_info', 'IfcGUID', 'level', 'No', 'name', 'wall_finish', 'ceiling_finish', 'floor_finish')
        skip_unchanged = False
        report_skipped= False

class RoomAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('project_info', 'level', 'No', 'name', 'wall_finish', 'ceiling_finish', 'floor_finish', )
    list_filter = ('project_info', 'level')
    readonly_fields = ('project_info', 'IfcGUID', 'level', 'No', 'name',)
    base_formats.CSV.CONTENT_TYPE = 'text/csv; charset=CP932'
    resource_class = RoomResource



admin.site.register(Project_info, Project_infoAdmin )
admin.site.register(Level, LevelAdmin )
admin.site.register(Wall_finish, Wall_finishAdmin )
admin.site.register(Ceiling_finish, Ceiling_finishAdmin )
admin.site.register(Floor_finish, Floor_finishAdmin )
admin.site.register(Room, RoomAdmin )

