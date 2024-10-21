"""

Sample bot that wraps Claude-3-Haiku but makes responses Haikus

"""

from __future__ import annotations

from typing import AsyncIterable

import fastapi_poe as fp

from poe_agent.config import API_KEY

from poe_agent.prompts.chatgpt import GPT_PROMPT


import fastapi_poe as fp

MODEL = 'Gemini-1.0-Pro'

# Replace the bot name and access key with information of your bot
# bot_name = "digit-test-bot"
# access_key = API_KEY

# fp.sync_bot_settings(bot_name, access_key)


class PromptBot(fp.PoeBot):
    async def get_response(
        self, request: fp.QueryRequest
    ) -> AsyncIterable[fp.PartialResponse]:
        request.query = [
            fp.ProtocolMessage(role="system", content=GPT_PROMPT)
        ] + request.query
        async for msg in fp.stream_request(
            request, MODEL, request.access_key
        ):
            yield msg

    async def get_settings(self, setting: fp.SettingsRequest) -> fp.SettingsResponse:
        return fp.SettingsResponse(server_bot_dependencies={MODEL: 1})


if __name__ == "__main__":
    fp.run(PromptBot(), allow_without_key=True)
