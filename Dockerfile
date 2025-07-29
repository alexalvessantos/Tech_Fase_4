# Usa uma imagem leve do Python 3.10
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos da raiz do projeto para o diretório /app no container
COPY . .

# Instala as dependências a partir do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 usada pelo Flask e pelo Gunicorn
EXPOSE 5000

# Comando para iniciar a aplicação usando Gunicorn, apontando para o objeto app dentro de api/main.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api.main:app"]
