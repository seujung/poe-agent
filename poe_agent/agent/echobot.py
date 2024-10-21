import fastapi_poe as fp
from poe_agent.config import API_KEY


# Replace the bot name and access key with information of your bot
bot_name = "agent-test-bot"
access_key = "nAvYwW5plq3rTD2FZx1quH86jbMc7Ql1"

# fp.sync_bot_settings(bot_name, access_key)

class EchoBot(fp.PoeBot):
    async def get_response(self, request: fp.QueryRequest):
        last_message = request.query[-1].content
        yield fp.PartialResponse(text=last_message)

if __name__ == "__main__":
    # fp.run(EchoBot(), allow_without_key=True)
    fp.run(EchoBot(), access_key=API_KEY)