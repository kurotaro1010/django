from django.shortcuts import render, redirect
from .forms import PostForm, RecordNumberForm, SetOrderOption
from .models import *
from django.core.paginator import Paginator

# now_pageがない時は1ページ目を表示するように設定
def index(request, now_page=1):
    # レコード件数:'record_number'は辞書のキーと思っておく。単なる文字列でない。
    if 'record_number' in request.session:
        record_number = request.session['record_number']
    else: 
        record_number = 10

    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

# 新着順・古い順
    if 'order_option' in request.session:
        order_option = request.session['order_option']
    else:
        order_option = 'new'
    # print(order_option)

    order_number_option = SetOrderOption()
    order_number_option.initial = {'order_option': str(order_option)}

# 新着順・古い順での設定
    if order_option == 'new':
        memos = Memo.objects.all().order_by('update_datetime').reverse()
    else:
        memos = Memo.objects.all().order_by('update_datetime')

    page = Paginator(memos, record_number)
    params = {
      'page': page.get_page(now_page),
      'form': PostForm(),
      'record_number_form': record_number_form,
      'order_number_option': order_number_option,
    }
    return render(request, 'index.html', params)

def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    return redirect(to='/')

def set_record_number(request):
    request.session['record_number'] = request.POST['record_number']
    return redirect(to='/')

def set_order_option(request):
    # print('a')
    request.session['order_option'] = request.POST['order_option']
    return redirect(to='/')