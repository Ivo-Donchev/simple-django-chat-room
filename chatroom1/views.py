from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm, LoginForm
from django.views.generic.edit import FormView

decorators = [login_required]


class MessagesList(ListView):
    model = Message
    context_object_name = 'messages'


@method_decorator(login_required, name='dispatch')
class Index(TemplateView):
    template_name = "chatroom1/index.html"


@method_decorator(login_required, name='dispatch')
class Chat_room_class_based(FormView):
    template_name = 'chatroom1/chat_form.html'
    form_class = MessageForm
    success_url = ''
    
    def form_valid(self, form):
        messages = Message.objects.all()
        Message.objects.create(message=form.cleaned_data['message'],
                               publisher=self.request.user.username)
        print(locals())
        # return redirect('/chatroom/class-based-view', locals())
        return render(self.request, self.template_name, locals())

    def form_invalid(self, form):
        messages = Message.objects.all()
        print(locals())
        return render(self.request, self.template_name, locals())


def create_message(message, publisher, added=False):
    Message(message=message, publisher=publisher, added=added).save()


def chat_room(request):
    # Message.objects.all().delete()
    if request.user.is_authenticated() is False:
        return redirect(log_in)
    messages = Message.objects.all()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['message']
            owner = request.user.username
            added = False
            create_message(text, owner, added)
        return redirect(chat_room)
    else:
        form = MessageForm()

    return render(request, 'chatroom1/chat_room.html', locals())


def update_messages(request):
    print(request.user.username)
    content_type = request.META.get("CONTENT_TYPE", "text/html")

    updated_messages = Message.objects.filter(added=False).\
        exclude(publisher=request.user.username)

    print(updated_messages)
    for e in updated_messages:
        e.added = True
        e.save()

    if content_type == "text/html":
        return render(request, 'chatroom1/ajax_test.html', locals())

    if content_type == "application/json":
        return JsonResponse({})


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect(chat_room)
    else:
        form = LoginForm()
    return render(request, 'chatroom1/chat_room.html', locals())
