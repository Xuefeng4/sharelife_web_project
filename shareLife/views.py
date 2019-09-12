from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from message.models import Message
from .forms import SubmitPostForm, SearchPostForm
from message.form import MessageForm
from .models import Post, User, PostDetail,Location
from django.views import View

from .models import Post, User
from .forms import SubmitPostForm



def index(request):
    if request.user.is_authenticated:
        post_list = Post.objects.all().exclude(author=request.user).order_by('-created_time')[:10]
        user_posts = Post.objects.filter(author=request.user).order_by('-created_time')
    else:
        user_posts = []
        post_list = Post.objects.all().order_by('-created_time')[:10]


    searchForm = SearchPostForm()
    return render(request, 'index.html', context={'post_list':post_list, 'user_list':user_posts, 'search_form':searchForm})

def form(request):
    if request.method == 'POST':  

        form = SubmitPostForm(request.POST)
        #TODO: not authenticated error
        if not request.user.is_authenticated:
            pass
        else:
            if form.is_valid():
                name = form.cleaned_data['name']
                body = form.cleaned_data['body']
                location = form.cleaned_data['location']

                # created_time = models.DateTimeField()
                # modified_time = models.DateTimeField()
                p = Post(name=name, body=body,
                        created_time=timezone.now(), modified_time=timezone.now(),
                         author=request.user,
                         pic_url ="https://a0.muscache.com/im/pictures/3423348/5d067377_original.jpg?aki_policy=large")
                p.save()
                return HttpResponseRedirect(reverse('shareLife:index'))

    else:  #first
        form = SubmitPostForm()
    return render(request, 'form.html', {'form': form})


class updatePost(UpdateView):
    model = Post
    fields = ["name", "body","location", "address", 'startDate', 'endDate']
    labels = {'body': "Introduction"}
    help_texts = {'body': 'Tell us about your place' }
    success_url = reverse_lazy('shareLife:index')

class deletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('shareLife:index')

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # detail = get_object_or_404(PostDetail, pk = pk)
    print(request)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    # 记得在顶部导入 CommentForm
    form = MessageForm()
 
    message_list = Message.objects.all().filter(post =pk)
    amenity_text = post.get_amenity()
    print(type(amenity_text))
    context = {'post':post,'message_form': form,'message_list': message_list,'amen_list':amenity_text}
    return render(request, 'detail.html', context=context)

def search(request):
    path = request.path

    #time location bedrooms, tag
    city_center = [(40.7128,74.0060)]
    if request.method == 'GET':
        bedrooms = request.GET.get('bedrooms')
        bathrooms =request.GET.get('bathrooms')
        location =  request.GET.get('location') # return id
        startDate = request.GET.get('startDate')
        endDate = request.GET.get('endDate')

        condition = "&bedrooms=%s&bathrooms=%s&location=%s&startDate=%s&endDate=%s"%(bedrooms,bathrooms,location,startDate,endDate)
        print(condition)
        error_msg = ''
        print(bedrooms)
        print(type(bathrooms))

        post_list1 = Post.objects.filter(bedrooms=bedrooms)
        post_list2 = Post.objects.filter(location=location)
        post_list3 = Post.objects.filter(startDate__lte= startDate) & Post.objects.filter(endDate__gte= endDate)
        post_list4 = Post.objects.filter(bathrooms__icontains = bathrooms)

        print(len(post_list1))
        print(len(post_list2))
        print(len(post_list3))
        print(len(post_list4))

        post_list12 = post_list1 & post_list2
        post_list13 = post_list1 & post_list3
        post_list14 = post_list1 & post_list4
        post_list23= post_list2 & post_list3
        post_list24 =post_list2 & post_list4
        post_list34 = post_list3 & post_list4

        post_listSum2  = (post_list12|post_list23|post_list14|
                          post_list23|post_list24|post_list34).distinct()

        post_list123 = post_list12 & post_list3
        post_list234 = post_list23 & post_list4
        post_list124 = post_list12 & post_list4
        post_list134 = post_list13 & post_list4

        post_listSum3  = (post_list123|post_list234|post_list134|
                          post_list124).distinct()

        post_listSum4 = (post_list12 & post_list34).distinct()

        post_listSum3 = post_listSum3.difference(post_listSum4)

        post_listSum2 = post_listSum2.difference(post_listSum4).difference(post_listSum3)
        numofCons = []
        numofCons += [4]* len(post_listSum4)
        numofCons += [3]* len(post_listSum3)
        numofCons += [2]* len(post_listSum2)

        num4 = len(post_listSum4)
        num3 = len(post_listSum3)
        num2 = len(post_listSum2)

        post_listSum4 = post_listSum4 | post_listSum3
        post_listSum4 = post_listSum4 | post_listSum2



        paginator = Paginator(post_listSum4, 10)
        paginatorN = Paginator(numofCons, 10)

        page = request.GET.get('page')


        try:
            post_listSum4 = paginator.page(page)
            consParams = paginatorN.page(page)
        except PageNotAnInteger:
            post_listSum4 = paginator.page(1)
            consParams = paginatorN.page(1)
        except EmptyPage:
            post_listSum4 = paginator.page(paginator.num_pages)
            consParams = paginatorN.page(paginatorN.num_pages)

        ret = list(zip(consParams, list(post_listSum4)))


        return render(request, 'result.html', {'error_msg': error_msg, 'post_list4':ret,'post_list':post_listSum4,
                                               'condition':condition, 'num2':num2,'num3':num3,'num4':num4})



