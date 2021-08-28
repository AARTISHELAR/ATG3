from django.shortcuts import render
from home.structure_data import *
from home.models import  intresting_url,unintresting_url

# Create your views here.
def home(request):
    link1 = get_internshala_post_link()
    link2 = get_iimjobs_post_link()
    link3 = get_talenttrack_post_link()
    for url in link1:
        data = get_ld_json2(url)
        if isinstance(data, dict):
            store_data(data)
            In = intresting_url(url = url)
            In.save()


    for url in link2:
        data = get_ld_json1(url)
        print(isinstance(data, dict))
        if isinstance(data, dict):
            store_data(data)
            In = intresting_url(url = url)
            In.save()
        elif data != 'structure data':
            In = unintresting_url(url = url)
            In.save()


        
    for url in link3:
        data = get_ld_json1(url)
        print(isinstance(data, dict))
        if isinstance(data, dict):
            store_data(data)
            In = intresting_url(url = url)
            In.save()
        elif data != 'structure data':
            In = unintresting_url(url = url)
            In.save()
    return render(request,'home.html')