FROM nginx:alpine

# Copy custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static app files
COPY index.html /usr/share/nginx/html/index.html
COPY scripts.json /usr/share/nginx/html/scripts.json
COPY audio/ /usr/share/nginx/html/audio/

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
