# 使用最輕量化的 Nginx 伺服器作為基礎鏡像
FROM nginx:alpine

# 這裡不需要寫複雜的東西，只要有這行，Docker 就知道怎麼打包
# 我們可以加一行指令，讓它在啟動時印出 "Hello DevOps"
RUN echo "<h1>Hello DevOps! My CI/CD is working!</h1>" > /usr/share/nginx/html/index.html

# 暴露 80 端口
EXPOSE 80
