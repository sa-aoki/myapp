from django import forms
from .models import Project_info, Level, Room, Wall_finish, Ceiling_finish, Floor_finish, Document
from django.forms import ModelForm 
from .models import Document



#部屋
class RoomForm(forms.ModelForm):
   
  #  def __init__(self, *args, **kwargs):
  #       super().__init__(*args, **kwargs)
  #       self.fields['project_info'].widget.attrs['disabled'] = 'disabled'
  #       self.fields['IfcGUID'].widget.attrs['disabled'] = 'disabled'
  #       self.fields['level'].widget.attrs['disabled'] = 'disabled'
  #       self.fields['No'].widget.attrs['disabled'] = 'disabled'

  class Meta:
        model = Room
        fields = ['wall_finish', 'ceiling_finish', 'floor_finish']




#アップロードファイル
class DocumentForm(forms.ModelForm):
    
  class Meta:
    model = Document
    fields = '__all__'



#プルダウン
class PDForm(forms.Form):
    
    project_info = forms.ModelChoiceField(
      label='プロジェクトID',
      required=True,
      disabled=False,
      queryset=Project_info.objects.all(), 
      widget=forms.Select
        )
    
    level = forms.ModelChoiceField(
          label='レベル',
          required=True,
          disabled=False,
          queryset=Level.objects.all(), 
          widget=forms.Select
        )


    wall_finish = forms.ModelChoiceField(
          label='壁仕上',
        #   required=True,
          disabled=False,
          queryset=Wall_finish.objects.all(), 
          widget=forms.Select(attrs={
               'id': 'name',}))


    ceiling_finish = forms.ModelChoiceField(
          label='天井仕上',
        #   required=True,
          disabled=False,
          queryset=Ceiling_finish.objects.all(),
          widget=forms.Select(attrs={
               'id': 'name',}))
    

    floor_finish = forms.ModelChoiceField(
          label='床仕上',
        #   required=True,
          disabled=False,
          queryset=Floor_finish.objects.all(),
          widget=forms.Select(attrs={
               'id': 'name',}))
    


    

