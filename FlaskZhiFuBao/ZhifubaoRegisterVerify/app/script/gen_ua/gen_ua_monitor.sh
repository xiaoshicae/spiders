#!/bin/sh
ps -fe|grep gen-UA-jar-with-dependencies|grep -v grep
if [ $? -ne 0 ]
then
echo "start process gen-UA ....."
nohup java -jar  gen-UA-jar-with-dependencies.jar >/dev/null 2>&1 &
else
echo "gen-UA still running....."
fi
