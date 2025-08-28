# Usando a imagem oficial do Node como base
FROM node

# Define o diretório de trabalho dentro do container (/app)
# Todos os próximos comandos serão executados dentro dessa pasta
WORKDIR /app

# Copia os arquivos de dependências (package.json e package-lock.json)
# Isso permite que o Docker use cache para instalar dependências,
COPY package*.json .

# Instala as dependências do projeto dentro do container
RUN npm install

# Copia todo o restante dos arquivos da aplicação para dentro do container
COPY . .

# Expõe a porta 3000, que será usada para acessar a aplicação
EXPOSE 3000

# Inicia a aplicação com Node rodando o arquivo app.js
CMD ["node", "app.js"]
