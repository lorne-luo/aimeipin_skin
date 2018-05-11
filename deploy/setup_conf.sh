ln -s `pwd`/nginx_ozsale_uwsgi.conf  /usr/local/nginx/conf/vhost/ozsales.conf
ln -s `pwd`/nginx_supervisord.conf /usr/local/nginx/conf/vhost/supervisord.conf
ln -s `pwd`/supervisord_ozsales.conf /etc/supervisor/supervisor.d/ozsales.conf
