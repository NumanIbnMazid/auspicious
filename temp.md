
# Digital Ocean Droplet Information

    - IP Address: 188.166.237.192
    - ssh root@188.166.237.192
    - aUspicious@2021A


server {
    listen 80;
    server_name auspicious.com.bd www.auspicious.com.bd 209.97.167.71;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/Auspicious;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}