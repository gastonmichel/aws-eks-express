FROM --platform=linux/amd64 node:14
WORKDIR /app
RUN npx express-generator
RUN npm install
CMD [ "npm", "start" ]