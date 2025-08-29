# Definindo a imagem base:Python versão3
FROM python:3

#Verifica se a pasta "/app" existe dentro da imagem.
# Se não existir → ele cria automaticamente | Se já existir → ele só muda para lá.
WORKDIR /app

RUN pip install flask 
RUN pip install requests

# O projeto será copiado para dentro da pasta /app, no container
COPY . . 

EXPOSE 5000

# Executa...
CMD ["python", "./app.py"]

# 1) Built image: docker build -t flaskexterna .
# 2) Run container: docker run -d -p 5000:5000 --name flask_externo_container flaskexterna