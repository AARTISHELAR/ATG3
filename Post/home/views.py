from django.shortcuts import render
from home.structure_data import *
from home.models import  intresting_url,unintresting_url,Category

# Create your views here.
def home(request):
    link1 = get_internshala_post_link()
    link2 = get_iimjobs_post_link()
    link3 = get_talenttrack_post_link()
    
    group1 = Category.objects.get(name = 'Graphic Design')
    group2 = Category.objects.get(name = 'Finance')
    iterate_link(link1,group1)
    iterate_links(link2,group2)
    iterate_links(link3,group1)
    
    return render(request,'home.html')