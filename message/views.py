from django.shortcuts import render, get_object_or_404, redirect
from shareLife.models import Post
from django.http import Http404,HttpResponse, HttpResponseRedirect
from .form import MessageForm
from django.contrib.auth.models import User
from .models import  Message

# Create your views here.
def detailPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':

        form =  MessageForm(request.POST)
        print(request)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.post = post
            comment.sender = request.user
            comment.receiver = post.author

            comment.save()

            return redirect(post)

        else:
          
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return Http404

    return redirect(post)



def chatRoom(request, user1, user2, post):
    message_list1 = Message.objects.all().filter(sender = user1).filter(receiver =user2).filter(post=post)
    message_list2 = Message.objects.all().filter(sender = user2).filter(receiver =user1).filter(post=post)

    message_list = (message_list1|message_list2).order_by("time")[:20]
    form = MessageForm
    print(len(message_list))
    post = get_object_or_404(Post, pk=post)
    return render(request, "chatroom.html", {"user1":user1, "user2":user2, "post":post,
                                             "chats":message_list,"message_form":form})


def chatPost(request, post,  user1, user2):
    if request.method == 'POST':
        print("chatpost")
        post = get_object_or_404(Post, pk=post)


        print("eellll")
        form = MessageForm(request.POST)
        print(request.user)
        print(user1)
        print(user2)

        if form.is_valid():

            us2 = get_object_or_404(User,pk=user2)
            comment = Message(post = post, sender = request.user, receiver =us2, content = form.cleaned_data['content'])
            comment.save()
            return HttpResponseRedirect('/message/post/'+str(post.pk)+'/'+str(user1) +'/'+str(user2))

        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return Http404
    return redirect(request.path)
