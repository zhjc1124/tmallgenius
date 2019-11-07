# tmallgenius

本项目只提供一个自动读取指令并控制电脑发出语音的工具。

由于淘宝直接登录较为困难，所以间接利用淘宝的微博快捷登录功能，通过用微博账号密码来登录淘宝绕过检测。

## 注意事项

请**不要依赖此脚本**，此脚本的局限性相当的大，只是我一时兴起的产物。

不能解决目前出现的非语音打卡的任务。

本脚本运行时间较长，平均时间为10s，请耐心等待。

如出现各种问题，可将文件夹下的`tmallgenius.log`文件提交给我以便排查Bug。

## 环境要求

一台24小时联网运行的放在天猫精灵旁边的有麦克风的电脑。以下教程以Win10为例。

## 配置环境

### 1. 安装Chrome

这里给出官网下载链接：[https://www.google.cn/chrome/](https://www.google.cn/chrome/)

版本要求：`78正式版`，已安装过的可以跳过

检查版本号的方式如下：

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/chrome_version.jpg)

### 2. 安装Python

这里给出官方Python 3.7.5 32bit的下载链接：[https://www.python.org/ftp/python/3.7.5/python-3.7.5.exe](https://www.python.org/ftp/python/3.7.5/python-3.7.5.exe)

需要其他版本的请自行前往 [官网](https://www.python.org/) 下载

版本要求：`Python3+`，已安装过的可以跳过

安装时务必勾选上add to path, 如下图所示：

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/python_install.jpg)

### 3. 安装依赖包

在命令提示符或者Powershell下运行

> pip install pyttsx3 selenium

成功安装提示如下：

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/pip_install.jpg)

### 4. 淘宝账号绑定微博

请在[淘宝登录界面](https://login.taobao.com/member/login.jhtml) 如下图方式进行微博和淘宝账号的绑定，以确保用你的微博账号可以登录你的淘宝。

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/taobao_login.jpg)

## 程序调试

### 1. 下载项目

将此项目下载下来并解压，下载链接为：[https://codeload.github.com/zhjc1124/tmallgenius/zip/master](https://codeload.github.com/zhjc1124/tmallgenius/zip/master)

### 2. 配置账号密码

双击运行文件夹下的`test.bat`文件，按照提示输入你的**微博账号和密码**，如不出意外，等待脚本运行完毕后，电脑会自动播放出今日的指令。

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/check_test.jpg)

### 3. 添加系统计划任务

你可以用记事本修改文件夹下的`创建计划任务.bat`文件来修改脚本每天定时运行的时间，如下图所示。

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/edit_sched.jpg)

然后双击此文件，系统将自动添加进计划任务。

你可以在菜单栏中找到**任务计划程序**中找到此任务。

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/win_menu.jpg)

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/schedule.jpg)

你也可以运行**任务计划程序**中的此任务来测试脚本是否正常工作。

## 其他

你可能需要关闭电脑的自动睡眠

![](https://github.com/zhjc1124/tmallgenius/blob/master/pictures/no_sleep.jpg)