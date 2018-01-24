#!/bin/sh
ps -fe|grep Grab_ip_xundaili.py |grep -v grep
if [ $? -ne 0 ]
then
echo "start process xundaili ....."
nohup /home/software/anaconda3/bin/python /home/Interface/Proxy_pool/app/script/Grab_ip_xundaili.py >/dev/null 2>&1 &
else
echo "Grab_ip_xundaili still running....."
fi
