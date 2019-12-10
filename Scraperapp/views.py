from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4 

# Create your views here.

def home(req):
    # return HttpResponse('Hello, World')
    # names=['jyoti','ram','hari']
    # d={
        
    #     'names': names,
    #     'college': 'ncit'
    # }

    

    page=requests.get('https://fabpedigree.com/james/mathmen.htm')

    soup=bs4.BeautifulSoup(page.content,'html.parser')
    lists=[]
    links=soup.find_all('li')

    for link in links:
        s=link.find('a')
        lists.append(s.get_text())

    # for x in range(len(lists)): 
    #     print (lists[x]) 

    d={
      
        'lists':lists


     }    



   
    # name of dictionary
    return render(req,'home.html',d)   #or d only

def bootcamp(req):
    return HttpResponse('Hello, bootcamp')    