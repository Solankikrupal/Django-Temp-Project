from django.shortcuts import render


# Create your views here.
def index(call):
    my_dict = {
        'intro':'Hello World','data':14265
    }

    return render(call,'basic_app/index.html',my_dict)

def first(call):
    return render(call,'basic_app/first_page.html')

def relative(call):
    return render(call,'basic_app/relative_url_template.html')
