echo off
set t=00:01
echo 你将要设置每天启动的时间为%t%
echo 如果要覆盖任务计划的话，请右键以管理员身份运行
SCHTASKS /CREATE /SC DAILY /TN tmallgenius /TR %~dp0% %run.vbs /ST %t%
PAUSE