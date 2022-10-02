ARG NODE_VERSION=16.8.0-buster

FROM node:${NODE_VERSION} as develop-stage

ARG BUILD_ENVIRONMENT=local

RUN npm install -g @quasar/cli http-server

WORKDIR /app

COPY frontend/package*.json /app/

RUN npm install

CMD ["quasar", "dev", "-H", "0.0.0.0"]

FROM develop-stage as build-stage

COPY . ./

RUN npm install

RUN quasar build
WORKDIR /app/dist/spa
CMD ["quasar", "serve", "-H", "0.0.0.0", "-p", "8080"]

FROM nginx:1.21 as production-stage

COPY --from=build-stage /app/dist/spa /usr/share/nginx/html

COPY ./compose/default.conf /default.conf
COPY ./compose/start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]
