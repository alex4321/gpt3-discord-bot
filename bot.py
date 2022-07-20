import argparse
import json
import traceback
from discord import Client, Message
import discord.utils
import langdetect
from google.cloud import translate_v3
import openai


DEFAULT_GENERATION_PARAMS = {
    "temperature": 0.25,
    "engine": "text-davinci-002",
    "frequency_penalty": 1.0,
    "presence_penalty": 1.0
}


class Generator:
    def __init__(self, translation_cred: dict, gpt_key: str) -> None:
        self._translator = translate_v3.TranslationServiceClient.from_service_account_info(translation_cred["account"])
        self._translator_parent = translation_cred["parent"]
        openai.api_key = gpt_key
    
    def _translate(self, text: str, target_lang: str) -> str:
        req = translate_v3.TranslateTextRequest(contents=[text], target_language_code=target_lang, parent=self._translator_parent)
        return self._translator.translate_text(req).translations[0].translated_text

    def generate(self, text: str, params: dict) -> str:
        source_lang = langdetect.detect(text)
        if source_lang != "en":
            gpt_prompt = self._translate(text, "en")
        else:
            gpt_prompt = text
        params = dict(DEFAULT_GENERATION_PARAMS, **params)
        completion = openai.Completion.create(
            prompt=gpt_prompt,
            **params
        )
        if len(completion.choices) == 0:
            generation = ""
        else:
            generation = completion.choices[0].text
        generation = generation.strip()
        if source_lang != "en" and generation != "":
            generation = self._translate(generation, source_lang)
        return generation


class DiscordGenerationBot(Client):
    def __init__(self, generator: Generator, discord_token: str, on_error_message: str):
        super(DiscordGenerationBot, self).__init__()
        self.generator = generator
        self.discord_token = discord_token
        self.on_error_message = on_error_message
    
    async def on_message(self, message: Message) -> None:
        text : str = message.content.strip()
        if not text.lower().startswith("gpt3:"):
            return
        content = text[5:].strip()
        if content == "":
            if message.reference is not None:
                channel = self.get_channel(message.reference.channel_id)
                reference = await channel.fetch_message(message.reference.message_id)
                content = reference.content
            else:
                return
        if content[0] == "{" and "}" in content:
            content = content[1:]
            params_json = "{" + content.split("}")[0] + "}"
            content = "}".join(content.split("}")[1:])
        else:
            params_json = "{}"
        try:
            params = json.loads(params_json)
            try:
                generated = self.generator.generate(content, params)
                answer = content + " " + generated
            except:
                answer = self.on_error_message
                traceback.print_exc()   
        except:
            answer = "Invalid params"
        await message.channel.send(answer, reference=message)
    
    def run(self) -> None:
        super(DiscordGenerationBot, self).run(self.discord_token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    config_fname = parser.parse_args().config
    with open(config_fname, "r") as src:
        config_json = json.load(src)
    generator = Generator(config_json["cloudTranslation"], config_json["openAiKey"])
    client = DiscordGenerationBot(generator, config_json["discordToken"], config_json["onErrorMessage"])
    client.run()
