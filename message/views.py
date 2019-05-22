from django.shortcuts import render, get_object_or_404, redirect
from shareLife.models import Post
from django.http import Http404,HttpResponse, HttpResponseRedirect
from .form import MessageForm
from django.contrib.auth.models import User
from .models import  Message

# Create your views here.
def detailPost(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form =  MessageForm(request.POST)
        print(request)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post
            comment.sender = request.user
            comment.receiver = post.author

            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()


            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            # return chatDisplay(request)
            return redirect(post)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return Http404

    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    # return chatDisplay(request)
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
    # return Http404
    if request.method == 'POST':
        print("chatpost")
        post = get_object_or_404(Post, pk=post)

        # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
        # 因此只有当用户的请求为 post 时才需要处理表单数据。

        print("eellll")
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = MessageForm(request.POST)
        print(request.user)
        print(user1)
        print(user2)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            us2 = get_object_or_404(User,pk=user2)
            comment = Message(post = post, sender = request.user, receiver =us2, content = form.cleaned_data['content'])

            # 将评论和被评论的文章关联起来。
            # comment.post = post
            # comment.sender = request.user
            # comment.receiver = user2
            # comment.content = form.cleaned_data['content']

            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            # return chatDisplay(request)
            return HttpResponseRedirect('/message/post/'+str(post.pk)+'/'+str(user1) +'/'+str(user2))

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return Http404

    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    # return chatDisplay(request)
    return redirect(request.path)
