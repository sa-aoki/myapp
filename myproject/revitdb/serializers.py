from rest_framework import serializers
from .models import Room, Project_info, Level

class RoomSerializer(serializers.ModelSerializer):
      class Meta:
            model = Room
            fields=('id', 'project_info', 'IfcGUID', 'level', 'No', 'name', 'wall_finish', 'ceiling_finish', 'floor_finish')
            read_only_fields = ['id', 'project_info', 'IfcGUID', 'level', 'No', 'name']

      def to_representation(self, instance):
        ret = super(RoomSerializer, self).to_representation(instance)
        # 部屋インスタンス
        project_info = instance.project_info
        # プロジェクト名
        ret["project_info_name"] = project_info.name

        level = instance.level
        # レベル
        ret["level_name"] = level.name
        return ret
      

# class Project_infoSerializer(serializers.ModelSerializer):
#       class Meta:
#             model = Project_info
#             fields=('id', 'project_No', 'name', 'project_type')
#             read_only_fields = ['id', 'project_info', 'IfcGUID', 'level', 'No', 'name']

#       def to_representation(self, instance):
#         ret = super(Project_infoSerializer, self).to_representation(instance)
#         # 部屋インスタンス
#         room = instance.room
#         # 部屋名
#         ret["room_name"] = room.name

#         level = instance.level
#         # レベル
#         ret["level_name"] = level.name
#         return ret
      
# class LevelSerializer(serializers.ModelSerializer):
#       class Meta:
#             model = Level
#             fields=('id', 'project_No', 'name', 'project_type')
#             read_only_fields = ['id', 'Level', 'IfcGUID', 'level', 'No', 'name']

#       def to_representation(self, instance):
#         ret = super(LevelSerializer, self).to_representation(instance)
#         # レベルインスタンス
#         room = instance.room
#         # 部屋名
#         ret["room_name"] = room.name

#         project_info = instance.project_info
#         # プロジェクト名
#         ret["project_info_name"] = project_info.name
#         return ret