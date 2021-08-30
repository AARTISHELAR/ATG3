import requests
import json
from bs4 import BeautifulSoup
from django.utils.dateparse import parse_date
from home.models import post
from django.contrib.auth.models import Group
import logging
from home.models import  intresting_url,unintresting_url


def get_soup(url):
    logging.info(f'send the request to {url}')
    req = requests.get(url)
    if req.status_code == 200:
      logging.info(f'response recived {req.status_code}')

    soup = BeautifulSoup(req.text, 'lxml')
    return soup


def get_internshala_post_link():
    main_link = 'https://internshala.com/fresher-jobs/graphic%20design-jobs'
    soup = get_soup(main_link)
    logging.info('parse the internshala html document')
    links = []
    posts = soup.find('div',attrs={'id':'internship_list_container'}).div.find_all('div',class_='individual_internship')
    for p in posts:
        link = 'https://internshala.com' + p.find('a')['href']
        #print(link)
        links.append(link)
    logging.info('collected the urls  from internshala')
    logging.info('return the urls')
    return links

def get_iimjobs_post_link():
    main_link = 'https://www.iimjobs.com/c/finance-jobs-13.html'#'https://www.iimjobs.com/c/finance-jobs-13.html'
    soup = get_soup(main_link)
    logging.info('parse the iimjobs html document')
    links = []
    posts = soup.find_all('div',class_='jobRow')[:11]
    for p in posts:
        link = p.find('a')['href']
        #print(link)
        links.append(link)
    logging.info('collected the urls  from iimjobs')
    logging.info('return the urls')
    return links

def get_talenttrack_post_link():
    main_link ='https://www.talentrack.in/graphic-designer-job-in-india--age-0-75?page=1'
    soup = get_soup(main_link)
    logging.info('parse the talenttrack html document')
    links = []
    posts = soup.find('div',class_='job_result').find_all('div',class_='job-listing-new')
    for p in posts:
        link = 'https://www.talentrack.in' + p.find('a')['href']
        #print(link)
        links.append(link)
    logging.info('collected the urls  from talenttrack')
    logging.info('return the urls')
    return links

def get_ld_json2(url):
    soup = get_soup(url)
    #print(soup)
    logging.info('loads the json-ld data into dict in python')
    data = json.loads(''.join(soup.find_all("script", {"type":"application/ld+json"})[1].contents),strict=False)
    logging.info('return structure data in dict format')
    return data

def get_ld_json1(url):

    soup = get_soup(url)
    #print(soup)
    logging.info('loads the json-ld data into dict in python')
    try:
        data = json.loads(''.join(soup.find("script", {"type":"application/ld+json"}).contents),strict=False)
        logging.info('return structure data in dict format')
        return data
    except:
        logging.error('error occur while loads the json-ld data')
        logging.info('return')
        data = 'structure data'
        return data
    

def store_data(data,group):
    logging.info('start to store data...')
    #title
    title = data['title']
    logging.info('title')

    #company
    if isinstance(data["hiringOrganization"], dict):
        company = data["hiringOrganization"]['name']
    elif isinstance(data["hiringOrganization"], str):
        company = data["hiringOrganization"]
    logging.info('company name.')

    #address
    try:
        if isinstance(data["jobLocation"],list):
            address = data["jobLocation"][0]["address"]["addressLocality"]
        elif isinstance(data["jobLocation"],dict):
            address = data["jobLocation"]["address"]["addressLocality"]
        else:
            address = 'remote'
        logging.info('jonlocation')
    except:
        logging.error('job is remote')
        address = 'remote'

    #validthrough
    logging.info('validthrough')
    validthrough = parse_date(data["validThrough"])
    #datePosted
    logging.info('dateposted')
    datePosted = parse_date(data["datePosted"])
    logging.info('save the post')
    p = post(title = title,company = company,address=address,validthrough=validthrough,datePosted=datePosted,category=group)
    p.save()

def iterate_links(links,group):
    for url in links:
        data = get_ld_json1(url)
        print(isinstance(data, dict))
        if isinstance(data, dict):
            store_data(data,group)
            logging.info(f'add in {group}')
            In = intresting_url(url = url)
            In.save()
        elif data != 'structure data':
            In = unintresting_url(url = url)
            In.save()
def iterate_link(links,group):
    for url in links:
        data = get_ld_json2(url)
        if isinstance(data, dict):
            store_data(data,group)
            logging.info(f'add in {group}')
            In = intresting_url(url = url)
            In.save()






        



