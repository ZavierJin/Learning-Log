# Learning-Log
学习笔记Web应用程序（python）

用户能够记录感兴趣的主题，并在学期每个主题的过程中添加日志条目。
主页对这个网站进行描述，并邀请用户注册或登录。
用户登录后，可以创建新主题、添加新条目以及阅读既有条目。
记录学到的知识可以帮助跟踪和复习这些知识。

项目名：learning-log

应用程序：
learning-logs
users

新修改：
测试时间2019/12/20，因为django包的问题，测试出了点bug，但是重新安装+更改代码后解决
django 版本2.0.5

在网页上运行程序的使用方法：（先确保安装python、django和django-bootsraps3）
①按win+r，输入cmd，打开cmd，输入指令：cd Learning-log文件夹地址，进入Learning-log文件夹目录
②激活虚拟环境。输入指令：ll_env\Scripts\activate
③运行程序。输入指令：python manage.py runserver
④在浏览器输入http://127.0.0.1:8000即可打开