echo off
SCHTASKS /CREATE /SC DAILY /TN tmallgenius /TR %~dp0% %run.vbs /ST 00:01
PAUSE