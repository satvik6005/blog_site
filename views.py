from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog import forms
import mysql.connector

def db_init():
    mydb = mysql.connector.connect(
        host="localhost",
        user="djangouser",
        password="password",
        database="blog_data",
        auth_plugin='mysql_native_password'
    )

    cur = mydb.cursor()
    return cur,mydb

def database_insert(t):
    cur,mydb=db_init()

    query = "insert into data (title,author,data_d) values(%s,%s,%s)"


    cur.execute(query, t)
    mydb.commit()
    mydb.close()



def database_list():
    cur,mydb=db_init()
    query = "Select * from data"


    cur.execute(query)
    data=cur.fetchall()
    mydb.commit()
    mydb.close()
    return data

def database_list():
    cur, mydb = db_init()
    query = "Select title,author,id from data"


    cur.execute(query)
    data=cur.fetchall()
    mydb.commit()
    mydb.close()
    return data

def database_vew(key):
    cur, mydb = db_init()

    query = "Select data_d,title,author from data where id=%s"



    cur.execute(query,(key,))
    data = cur.fetchall()
    print(data)
    mydb.commit()
    mydb.close()
    return data
def index(request):
    return render(request,'blog/index.html')
def list(request):

    try:
        data=database_list()
        print(data)
        data_dic={"data":data}

    except Exception as e:
        print(e)


    return render(request,'blog/list.html',context=data_dic)


def vew(request,data):
    blog=database_vew(data)
    dict_data={"data":blog[0][0],"title":blog[0][1],"author":blog[0][2]}

    return render(request, 'blog/view.html',context=dict_data)


def writting(request):
    if request.method=='POST':
        form=forms.blog_form(request.POST)
        if form.is_valid():
            t = (form.cleaned_data['title'], form.cleaned_data['author'], form.cleaned_data['data'])
            try:

                database_insert(t)
            except Exception as e :
                print(e)




            return redirect('index')

    form=forms.blog_form()

    return render(request, 'blog/writting.html',{'form':form} )

# Create your views here.
