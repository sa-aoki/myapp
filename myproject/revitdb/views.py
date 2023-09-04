from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Project_info, Level, Room, Wall_finish, Ceiling_finish, Floor_finish
from django.urls import reverse_lazy
from django.conf import settings
from . import forms
from .forms import PDForm, DocumentForm, RoomForm
from .filters import RoomFilter
from django_pandas.io import read_frame
import pandas as pd
from django.http import HttpResponse
import csv

#ログイン
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView):
    template_name = "top.html"

class Project_infoListView(LoginRequiredMixin, ListView):
    model = Project_info
    # template_name = "list.html"
    

class Wall_finishListView(LoginRequiredMixin, ListView):
    model = Wall_finish
    # template_name = "list.html"


class Ceiling_finishListView(LoginRequiredMixin, ListView):
    model = Ceiling_finish
    # template_name = "list.html"


class Floor_finishListView(LoginRequiredMixin, ListView):
    model = Floor_finish
    # template_name = "list.html"


#部屋リスト
# class RoomListView(LoginRequiredMixin, ListView):
#     model = Room
#     template_name = "revitdb/product_list.html"

#     def get_context_data(self, **kwargs):
#         # 既存のget_context_dataをコール
#         context = super().get_context_data(**kwargs)
#         # 追加したいコンテキスト情報(取得したコンテキスト情報のキーのリストを設定)
#         extra = {"extra": list(context.keys())}
#         # コンテキスト情報のキーを追加
#         context.update(extra)
#         return context
    
# class RoomUpdateView(UpdateView):
#     model = Room
#     # fields = '__all__'
#     form_class = RoomForm
#     template_name_suffix = '_update_form'
    
#     def get_success_url(self):
#         return reverse("product_list", kwargs={"pk":self.object.pk})


#部屋編集

def RoomUpdateView(request, pk):
    template_name = "revitdb/room_update_form.html"
    obj =Room.objects.get(pk=pk)
    initial_values = {"project_info": obj.project_info, "IfcGUID": obj.IfcGUID, "level": obj.level, "No": obj.No,  "name": obj.name, "wall_finish": obj.wall_finish, "ceiling_finish":obj.ceiling_finish, "floor_finish":obj.floor_finish}
    form =RoomForm(request.POST or initial_values)
    ctx = {"form": form}
    if form.is_valid():
        # project_info = form.data["project_info"].widget.attrs['readonly'] = True
        # IfcGUID = form.data["IfcGUID"].widget.attrs['readonly'] = True
        # level = form.data["level"].widget.attrs['readonly'] = True
        # No = form.data["No"].widget.attrs['readonly'] = True
        # name = form.data["name"].widget.attrs['readonly'] = True
        wall_finish = form.cleaned_data["wall_finish"]
        ceiling_finish = form.cleaned_data["ceiling_finish"]
        floor_finish = form.cleaned_data["floor_finish"]
        # obj.project_info = obj.project_info
        # obj.IfcGUID = obj.IfcGUID
        # obj.level = obj.level
        # obj.No = obj.No
        # obj.name = obj.name
        obj.wall_finish = wall_finish
        obj.ceiling_finish = ceiling_finish
        obj.floor_finish = floor_finish
        obj.save()
    return render(request, template_name, ctx)



#データダウンロード
# def room_export(request):
#     qs = Room.objects.all()
#     df = read_frame(qs)
#     exp_path = settings.MEDIA_ROOT / 'room_export.csv'
#     df.to_csv(exp_path, encoding='utf_8_sig',index=False)
#     return render(request, 'revitdb/room_export.html')



#プロジェクトとレベルでフィルタする部屋リスト
def product_list(request):
    f = RoomFilter(request.GET, queryset=Room.objects.all())
    return render(request, 'revitdb/product_list.html', {'filter': f})
    


#アップロードファイル
def modelform_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'modelform_upload.html',)
    else:
        form = DocumentForm()
    return render(request, 'modelform_upload.html', {
        'form': form
    })



#ログイン・ログアウト
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'




    #form
# def product(request):
#     form = PDForm()
#     # 入力結果を格納する辞書
#     results = {}
#     if request.method == 'POST':
#         # 入力されたデータの受取
#         results['project_info'] = request.POST["project_info"]
#         results['level'] = request.POST["level"]
#         results['wall_finish'] = request.POST["wall_finish"]
#         results['ceiling_finish'] = request.POST["ceiling_finish"]
#         results['floor_finish'] = request.POST["floor_finish"]
#         c = {'results': results}
#     else:    
#         form = forms.PDForm()
	    
#         form.fields['project_info'].initial = ['0']
#         form.fields['level'].initial = ['1']
#         form.fields['wall_finish'].initial = ['1']
#         form.fields['ceiling_finish'].initial = ['1']
#         form.fields['floor_finish'].initial = ['1']

#     return render(request,'revitdb/product.html',{'form': form,})

def office(request):
    print(request.GET.get("id"))
    return render(request, 'revitdb/product_list.html')
