# Usa uma imagem oficial do Python com menos camadas (mais leve)
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
# O ponto (.) significa tudo do diretório atual (inclusive subpastas)
COPY . .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pela aplicação Flask (via gunicorn)
EXPOSE 5000

# Comando para iniciar o servidor WSGI com gunicorn
# api.main:app significa:
#   - "api" é a pasta
#   - "main" é o nome do arquivo Python (main.py)
#   - "app" é a variável Flask dentro desse arquivo
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api.main:app"]
