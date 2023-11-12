FROM nginx:latest

LABEL maintainer="Rogério Peixoto"
LABEL description="Dockerfile for the app"

ARG VERSION

COPY index.html /usr/share/nginx/html/

COPY server.conf /etc/nginx/conf.d/

EXPOSE 80

RUN sed -i "s|<VERSION_PLACEHOLDER>|$VERSION|g" /usr/share/nginx/html/index.html