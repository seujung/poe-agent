
# ngrok 설정
from pyngrok import ngrok

# 로컬 포트 지정
port = 8000

# ngrok 실행
public_url = ngrok.connect(port)
public_url