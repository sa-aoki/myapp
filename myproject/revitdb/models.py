from django.db import models
from django.urls import reverse
    
    

#プロジェクト情報：モデル作成
class Project_info(models.Model):
    project_No= models.CharField(max_length=15, unique=True, verbose_name='設計番号')
    name = models.CharField(max_length=200, verbose_name = 'プロジェクト名', unique=True)
    project_type = models.CharField(max_length=200, verbose_name='工事種別')
    
    def __str__(self):
        return self.name
    
#レベル：モデル作成
class Level(models.Model):
    name = models.CharField(max_length=10, verbose_name = 'レベル名', unique=True)
    
    def __str__(self):
        return self.name
    


#壁仕上：モデル作成
class Wall_finish(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name = '仕上 壁')


    def __str__(self):
        return self.name
    
    
        # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('wall_finish_list')
    



#天井仕上：モデル作成
class Ceiling_finish(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name = '仕上 天井')

    def __str__(self):
        return self.name
    
    
        # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('ceiling_finish_list')
    
    


#床仕上：モデル作成
class Floor_finish(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name = '仕上 床')

    def __str__(self):
        return self.name
    

    
        # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('floor_finish_list')
    


#部屋：モデル作成
class Room(models.Model):
    project_info = models.ForeignKey(Project_info, verbose_name = 'プロジェクト名', on_delete=models.PROTECT)
    IfcGUID = models.CharField(max_length=200, unique=True )
    level = models.ForeignKey(Level, verbose_name='レベル', on_delete=models.PROTECT)
    No = models.CharField(max_length=200, verbose_name='部屋番号', unique=True)
    name = models.CharField(max_length=20, verbose_name='部屋名')
    wall_finish = models.ForeignKey(Wall_finish, verbose_name='仕上 壁', on_delete=models.PROTECT, blank=True, null=True)
    ceiling_finish = models.ForeignKey(Ceiling_finish, verbose_name='仕上 天井', on_delete=models.PROTECT, blank=True, null=True)
    floor_finish = models.ForeignKey(Floor_finish, verbose_name='仕上 床', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('room_list')
    

#Excelファイル：アップロード
class Document(models.Model):
    # description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

