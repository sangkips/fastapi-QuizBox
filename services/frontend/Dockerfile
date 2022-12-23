FROM node:lts-alpine

# Create app directory
WORKDIR /app

RUN npm install -g npm@9.2.0

RUN npm install @vue/cli@5.0.8 -g

# Install app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# Bundle app source
COPY . .

# Build the app
RUN npm run build

# Run the app
CMD ["npm", "run", "serve"]

