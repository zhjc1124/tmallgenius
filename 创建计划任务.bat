echo off
set t=00:01
echo �㽫Ҫ����ÿ��������ʱ��Ϊ%t%
echo ���Ҫ��������ƻ��Ļ������Ҽ��Թ���Ա�������
SCHTASKS /CREATE /SC DAILY /TN tmallgenius /TR %~dp0% %run.vbs /ST %t%
PAUSE