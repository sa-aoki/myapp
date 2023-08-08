from django.shortcuts import render, redirect
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
class RoomListView(LoginRequiredMixin, ListView):
    model = Room
    # template_name = "list.html"

    def get_context_data(self, **kwargs):
        # 既存のget_context_dataをコール
        context = super().get_context_data(**kwargs)
        # 追加したいコンテキスト情報(取得したコンテキスト情報のキーのリストを設定)
        extra = {"extra": list(context.keys())}
        # コンテキスト情報のキーを追加
        context.update(extra)
        return context
    
class RoomUpdateView(UpdateView):
    model = Room
    fields = '__all__'
    template_name_suffix = '_update_form'



#データダウンロード
def room_export(request):
    qs = Room.objects.all()
    df = read_frame(qs)
    exp_path = settings.MEDIA_ROOT / 'room_export.csv'
    df.to_csv(exp_path, encoding='utf_8_sig',index=False)
    return render(request, 'revitdb/room_export.html')





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
            return redirect('product_list')
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
