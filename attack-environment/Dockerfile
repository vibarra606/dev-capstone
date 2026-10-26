# Start from a lightweight web server image
FROM nginx:alpine

# We need to work on our fake Google Meet HTML file so this can go straight into the server's web directory
COPY ./index.html /usr/share/nginx/html/index.html

EXPOSE 80
