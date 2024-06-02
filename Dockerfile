#создаем образ python внутри контейнера
FROM python:3.6-slim

# копируем весь проект в образ директория у нас . директория в контейнере
COPY . /root

# рабочая директория Docker контейнера - указываем явно
WORKDIR /root

# устанавливаем flask внтури образа python
RUN pip install --upgrade pip
RUN pip install flask
