FROM python:3.9-slim
# On utilise une image slime pour réduire la taille de l'image finale
RUN pip install flask numpy matplotlib
# Les libraires nécessaires sont installées
WORKDIR /app
# On définit le répertoire de travail
COPY app.py .
# On copie le fichier de l'application dans le conteneur
CMD ["python", "app.py"]
# python app.py