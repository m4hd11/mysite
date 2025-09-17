from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.name = "Anonymous"
            if not ticket.subject:
                ticket.subject = None
            ticket.save()

            messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket didnt submited!')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

# def test_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('done')
#         else:
#             return HttpResponse('not valid!')
        
#     form = ContactForm()
#     return render(request, 'test.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "Please enter a valid email!")

        # بازگشت به همان فرم sidebar
        referer = request.META.get('HTTP_REFERER', '/')
        if '#' in referer:
            # اگر anchor دارد، اضافه نکن
            return redirect(referer)
        return redirect(referer + '#sidebar-newsletter')

