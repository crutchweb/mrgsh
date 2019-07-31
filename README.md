# daboboom

Python 3.4.3
PostgreSQL 9.3

Database:
db.json created via next command:
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json

for import use:
./manage.py loaddata db.json

reserve backup via pg_dump command:
https://yadi.sk/d/4C6morG3gHnB8Q

for import use:
pg_restore 

nginx config:

server {

    listen 80;
    server_name daboboom.ru; #либо ip, либо доменное имя
    access_log  /var/log/nginx/example.log;
    location /static/ {
        root /home/dabo/Projects/dabo-env/daboboom/;
        expires 30d;
    }
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
}


how to links:
<p>https://the-bosha.ru/2016/06/29/django-delaem-damp-bazy-dannykh-i-vosstanavlivaem-iz-nego-s-dumpdata-i-loaddata/</p>
<p>https://postgrespro.ru/docs/postgrespro/10/app-pgrestore</p>
