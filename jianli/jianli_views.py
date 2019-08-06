from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import FileResponse
from jianli.models import Visitor
def index(request):
    # return HttpResponse('hello world')
    if request.method == "GET":
        return render(request, 'jianli/jianli_index.html')
    else:
        visitor_name = request.POST.get('visitor_name')
        visitor_email = request.POST.get('visitor_email')
        visitor_text = request.POST.get('visitor_text')
        visitor_context = request.POST.get('visitor_context')
        visitor_tel = request.POST.get('visitor_tel')
        Visitor.objects.create(visitor_name=visitor_name,
                            visitor_email=visitor_email,
                            visitor_text=visitor_text,
                            visitor_context=visitor_context,
                            visitor_tel = visitor_tel)

        return redirect('jianli_index')
def about(request):
    # return HttpResponse('hello world')
    if request.method == "GET":
        return render(request, 'jianli/about.html')
    else:
        visitor_name = request.POST.get('visitor_name')
        visitor_email = request.POST.get('visitor_email')
        visitor_text = request.POST.get('visitor_text')
        visitor_context = request.POST.get('visitor_context')
        visitor_tel = request.POST.get('visitor_tel')
        Visitor.objects.create(visitor_name=visitor_name,
                               visitor_email=visitor_email,
                               visitor_text=visitor_text,
                               visitor_context=visitor_context,
                               visitor_tel=visitor_tel)

        return redirect('about')
def blog_post(request):
    # return HttpResponse('hello world')
    return render(request, 'jianli/blog_post.html')
def work_list(request):
    # return HttpResponse('hello world')
    return render(request, 'jianli/work_list.html')
def work_his(request):

    if request.method == "GET":
        return render(request, 'jianli/work_his.html')
    else:
        visitor_name = request.POST.get('visitor_name')
        visitor_email = request.POST.get('visitor_email')
        visitor_text = request.POST.get('visitor_text')
        visitor_context = request.POST.get('visitor_context')
        visitor_tel = request.POST.get('visitor_tel')
        Visitor.objects.create(visitor_name=visitor_name,
                               visitor_email=visitor_email,
                               visitor_text=visitor_text,
                               visitor_context=visitor_context,
                               visitor_tel=visitor_tel)

        return redirect('history')

def file_down(request):
    file=open('E:\\简历.doc','rb')
    response =FileResponse(file)
    response['Content-Type']='application/msword'
    response['Content-Disposition']='attachment;filename="简历.doc"'
    return response


