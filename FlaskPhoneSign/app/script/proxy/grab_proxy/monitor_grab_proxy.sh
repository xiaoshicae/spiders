#!/bin/sh
ps -fe|grep Grab_proxy_xundaili_wb.py |grep -v grep
if [ $? -ne 0 ]
then
echo "start process Grab_proxy_xundaili_wb ....."
nohup /home/software/anaconda3/bin/python /home/Interface/Flask_PhoneSign/app/script/proxy/grab_proxy/Grab_proxy_xundaili_wb.py&
else
echo "still runing....."
fi
