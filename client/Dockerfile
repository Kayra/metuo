FROM node:12.2.0-alpine as build
MAINTAINER Kayra Alat

RUN apk update
RUN apk upgrade --available

RUN mkdir /client
COPY . /client
WORKDIR /client

ENV PATH /client/node_modules/.bin:$PATH

COPY package.json /client/package.json
RUN npm install
RUN npm install react-scripts@3.0.1 -g
RUN npm audit fix
RUN npm run build

FROM nginx:1.16.0-alpine
COPY --from=build /client/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
