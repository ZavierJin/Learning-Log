""" 视图函数 """
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """ 学习笔记的主页 """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """ 只向用户显示自己的主题，并按添加时间排序 """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """ 显示单个主题及其所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404   # 引发Http404异常
    entries = topic.entry_set.order_by('-date_added')
    context = {'entries': entries, 'topic': topic}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """ 添加新主题 """
    if request.method != 'POST':    # 测试请求方法
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():     # 检查提交信息是否有效
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()     # 将表单数据写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """ 在特定的主题中添加新条目 """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """ 编辑既有条目 """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic.id]))   # ???

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
