'''
Created on 28-Nov-2015

@author: nell
'''
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango.settings')

import django
django.setup()

from rango.models import category, page

def populate():
    python_cat = add_cat('python',
                         )
    
    add_page(python_cat, 
             title= 'official python',
             url='http://blah blah blah......',
             )
    add_page(python_cat,
             title='fuvkin gpsf',
             url= 'www.zsdfgw.com',
             )
    add_page(python_cat,
             title='asssdifh',
             url= 'www.sdfgd.com',
             )
    
    django_cat = add_cat('django',
                         )
    
    add_page(django_cat,
             title= 'django official',
             url= 'www.zsg.com',
             )
    add_page(django_cat,
             title= 'srgerg icial',
             url= 'www.zsg.com',
             )
    
    nelson_cat = add_cat('nelson',
                         )
    
    add_page(nelson_cat,
             'nelson',
             'www.svf.com',
             )
    add_page(nelson_cat,
             'affbv',
             'www.sgethgebe.com',
             )
    
    rakesh_cat = add_cat('rakesh',
                         )
    
    add_page(rakesh_cat,
             'rakesh',
             'www.sgeg.com',
             )
    add_page(rakesh_cat,
             'aergerg',
             'www.aehteyj.com',
             )
    
    naveen_cat = add_cat('navven handlu',
                         )
    
    add_page(naveen_cat,
             'naveen',
             'www.handlu.com')
    
    for c in category.objects.all():
        for p in page.objects.filter(category = c):
            print ' - {0} - {1} '.format(str(c), str(p))
        
            
    
    
def add_page(cat, title, url, views=0):
    p = page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url
    p.views = views
    p.save()
   # return p

def add_cat(name, views=0, likes=0):
    c = category.objects.get_or_create(name = name)[0]
    c.views = views
    c.likes = likes
    return c

if __name__ == '__main__':
    print 'starting populating....'
    populate()
    print 'ending.....'