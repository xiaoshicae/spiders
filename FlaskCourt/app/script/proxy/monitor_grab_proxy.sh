#!/bin/sh
ps -fe|grep grab_proxy.py |grep -v grep
if [ $? -ne 0 ]
then
echo "start process....."
python grab_proxy.py
else
echo "still runing....."
fi