FROM node:alpine AS base

WORKDIR /src/app

COPY package*.json ./

COPY . ./

FROM base AS development

ENV NODE_ENV=development

RUN npm i

CMD [ "npm", "start" ]

FROM base AS production

ENV NODE_ENV=production

RUN npm ci --omit=dev

CMD [ "npm", "start" ]