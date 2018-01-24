#/bin/bash

echo "captcha_crack will be started ..."
cd /root/github/privateJob/Flask_App/CaptchaCrack
nohup /usr/local/bin/python /usr/local/bin/gunicorn -w 4 -b 127.0.0.1:5010 wsgi:application_captcha_crack&

echo "Grab_ip_xundaili.py will be started ..."
cd /root/github/privateJob/Flask_App/ProxyPool/app/script/GrabIP
nohup /usr/local/bin/python Grab_ip_xundaili.py&

echo "proxy_pool will be started ..."
cd /root/github/privateJob/Flask_App/ProxyPool
nohup /usr/local/bin/python /usr/local/bin/gunicorn -w 4 -b 127.0.0.1:5020 wsgi:application_proxy_pool&

echo "zhifubao_register_verify will be started ..."
cd /root/github/privateJob/Flask_App/ZhifubaoRegisterVerify
nohup /usr/local/bin/python /usr/local/bin/gunicorn -w 4 -b 127.0.0.1:5000 wsgi:application_zhifubao_register_verify&
