FROM nginx:latest

# Sao chép file index.html vào thư mục phục vụ của Nginx
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
