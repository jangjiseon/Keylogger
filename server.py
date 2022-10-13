from flask import Flask, request
from datetime import date, datetime

app = Flask(__name__)

@app.route('/get_logs', methods = ['POST'])
def get_logs():
    # 타인의 CLIENT로 부터 logs라는 파라미터의 form을 받아 logs에 저장
    logs = request.form['logs']

    # 저장한 log는 txt파일로 
    with open('logs.txt', 'a') as f:
        # 저장
        f.write(f'{datetime.now()} - {logs}\n')

    return {'result' : True}

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
