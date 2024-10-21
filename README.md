# poe-agent


### Setting
- ngrok 설정
   - https://ngrok.com/ 에 접속하여 token 생성

```bash
ngrok config add-authtoken <your_authtoken>
```



### Run
- fastapi
```bash
python poe_agent/agent/echobot.py --port 8080
```

외부 서버 노출
```bash
ngrok http 8080
```

### Reference
- https://github.com/poe-platform/server-bot-quick-start