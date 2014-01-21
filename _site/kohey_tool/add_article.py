# -*- coding: utf-8 -*-
import os
import sys
import datetime
args = sys.argv
dir_name = '/Users/kohey/Documents/Dev/Github/kohey18.github.com/_posts'
blog_dir = '~/Documents/Dev/Blog'
def writeForJekyll(blog_name,title,tag,updated_date):
    try:
        f = open(dir_name+'/'+blog_name,'w')
        print dir_name+'/'+blog_name
        # 文字列を出力
        new_blog_info = '---\n'
        new_blog_info +='layout:posts\n'
        new_blog_info +='title:'+title+'\n'
        new_blog_info +='description:\n'
        new_blog_info +='modified:'+updated_date+'\n'
        new_blog_info +='category: articles\n'
        new_blog_info +='tags: ['+tag+']\n'
        new_blog_info +='image:\n'
        new_blog_info +='---\n'
        print new_blog_info
        f.write(new_blog_info)
        f.close()
    except:
        print "error"



if len(args) ==4:
    blog_name = args[1]
    title = args[2]
    tag = args[3]
    print blog_name
    d = datetime.datetime.today()
    #2013-12-11-20131211.md
    blog_date = str(d.year)+'-'+str(d.month)+'-'+str(d.day)+'-'+str(d.year)+str(d.month)+str(d.day)+'_'+title+'.md'
    print blog_date
    #os.system ('cp '+blog_dir+'/'+blog_name+' '+dir_name+'/'+blog_name)
    #print ('cp '+blog_dir+'/'+blog_name+' '+dir_name+'/'+blog_name)
    updated_date = str(d.year)+'-'+str(d.month)+'-'+str(d.day)
    os.system ('cp '+blog_dir+'/'+blog_name+' '+dir_name+'/'+blog_date)
    writeForJekyll(blog_name,title,tag,updated_date)
    
    
    


else:

    print 'You should write like this!'
    print '(ex) python add_article.py hoge.md title tag'
