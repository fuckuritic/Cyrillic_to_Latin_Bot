FROM python:3.10-slim
ENV TOKEN='7349526718:AAGdPhPRvAZuSEt78Ru5XPnM3dnTU9P5ss0'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]