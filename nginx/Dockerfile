FROM nginx

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/project.conf
COPY project.conf /etc/nginx/conf.d/project.conf