#!/bin/sh
ps -fe|grep Grab_proxy_xundaili_zh.py |grep -v grep
if [ $? -ne 0 ]
then
echo "start process xundaili_zh ....."
nohup /home/software/anaconda3/bin/python /home/Interface/Proxy_pool/app/script/Grab_proxy_xundaili_zh.py&
else
echo "still runing....."
fi

ps -fe|grep Grab_proxy_ipserver.py |grep -v grep
if [ $? -ne 0 ]
then
echo "start process ipserver....."
nohup /home/software/anaconda3/bin/python /home/Interface/Proxy_pool/app/script/Grab_proxy_ipserver.py&
else
echo "still runing....."
fi
