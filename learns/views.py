from django.shortcuts import render

# Create your views here.
from datetime import datetime, date
from pkgutil import get_data

from django.shortcuts import render

# from django.shortcuts import render, get_object_or_404
# from learns.models import Post

# Create your views here.
all_posts=[
    {'slug':'cafsh_tabestani',
     'title':'کفش تابستانی',
     'cost':'قیمت:  400000 تومن',
     'date':datetime(2022,12,18),
     'image':'IMG_20240309_132945_231.jpg',
     'size':'سایز:38 تا 40',
    'Attributes':'مشکی، طوسی، کرم',
    'short_description':'کفش مجلسی بسیار زیبا و با دوام '
    },

    {'slug':'nim_boot',
     'title':'نیم بوت',
     'cost':'قیمت: 350000 تومن',
     'date':datetime(2019,11,17),
     'image':'79b6e866aae5e296647bec14868df4f64b6a39e0_1670399742.jpg',
     'size':'سایز:39 تا 41',
    'Attributes':'مشکی',
    'short_description':'چرم اصل، بسار راحت'
     },

    {'slug':'catooni_lej_dar',
     'title':'کتونی',
     'cost':'قیمت:  400000 تومن',
     'date':datetime(2020,12,17),
     'image':'IMG_20240309_132942_735.jpg',
     'size':'سایز: 38 تا 40 ',
    'Attributes':'سفید',
    'short_description':'قابل استفاده برای پیاده روی، بسیار راحت و زیبا'
     },

    {'slug':'sandal',
     'title':'صندل',
     'cost':'قیمت: 205000 تومن',
     'date':datetime(2021,12,17),
     'image':'IMG_20240309_132857_912.jpg',
     'size':'سایز:38 تا 41',
    'Attributes':'قهوه ای',
    'short_description':'برای استفاده روزمره و مهمانی'

     },
    {'slug':'cafsh_pashne_boland',
     'title':'کفش پاشنه بلند',
     'cost':'قیمت: 578000 تومن',
     'date':datetime(2020,12,17),
     'image':'IMG_20240309_132936_810.jpg',
     'size':'سایز:38 تا 41 ',
     'Attributes':'مشکی',
     'short_description':'جیر مصنوعی، مناسب روزمره و مهمانی '

     },
    {
    'slug':'catooni',
    'title':'کتونی ورزشی ',
    'cost':'قیمت:300000تومن',
    'date':datetime(2022,12,17),
    'image':'IMG_20240309_132940_588.jpg',
    'size':'سایز:38 تا 41',
    'Attributes':'مشکی',
    'short_description':'مناسب ورزش و روزمره'
    }

]



def get_data(post):
    return post['data']


def index(request):

    # return render(request,'learns/index.html',{'a':all_posts})
    sort_lst=sorted(all_posts,key=lambda x: x['date'])
    latest=sort_lst[-2:]
    return render(request, 'learns/index.html', {'latest':latest})

def posts(request):
    return render(request, 'learns/all_post.html', {'all_posts':all_posts})

def single_post(request,slug):
    post=next(post for post in all_posts if post['slug']==slug)
    # post=get_object_or_404(Post,slug=slug)
    return render(request, 'learns/post_detail.html', {'post':post})
