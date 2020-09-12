FROM python:3.7

COPY *.py /app/
COPY requirements.txt /app/
COPY Scores.txt /app/
EXPOSE 8777
WORKDIR /app
RUN python3.7 -m pip install -r requirements.txt
CMD python3.7 -u MainScores.py
