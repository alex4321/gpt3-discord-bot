# Discord GPT-3 bot

I made this Discord bot just for fun. 
It uses GPT-3 to autocomplete text, and Google Cloud Translation API to translate to English and back, if required.

Some examples:
```
Pino — Today at 4:50 PM
gpt3: Определите, относится ли текст к одной из областей, если нет - скажите как бы вы назвали его область.

Области:
- Информационные технологии
- Медицина
- Промышленность

Текст: импланты neurolink в сочетании с обработкой их данных посредством машинного обучения могут стать новым словом в протезировании
Выбранная область: Медицина, Информационные технологии

Текст: для приготовления курника нам понадобится тесто...
Выбранная область: ни одна из представленных, это кулинария

Текст: наконец запущен телескоп James Webb
Справка: Космический телескоп «Джеймс Уэбб» — орбитальная инфракрасная обсерватория. Самый крупный космический телескоп с самым большим зеркалом из когда-либо запущенных человечеством. Первоначально назывался «Космический телескоп нового поколения».
Выбранная область:

GPT3Bot
BOT
 — Today at 4:50 PM
Определите, относится ли текст к одной из областей, если нет - скажите как бы вы назвали его область.

Области:
- Информационные технологии
- Медицина
- Промышленность

Текст: импланты neurolink в сочетании с обработкой их данных посредством машинного обучения могут стать новым словом в протезировании
Выбранная область: Медицина, Информационные технологии

Текст: для приготовления курника нам понадобится тесто...
Выбранная область: ни одна из представленных, это кулинария

Текст: наконец запущен телескоп James Webb
Справка: Космический телескоп «Джеймс Уэбб» — орбитальная инфракрасная обсерватория. Самый крупный космический телескоп с самым большим зеркалом из когда-либо запущенных человечеством. Первоначально назывался «Космический телескоп нового поколения».
Выбранная область: астрономия
```

```
Pino - Today at 4:50 PM
gpt3: Determine if the text belongs to one of the areas, if not - say how you would name its area.

Areas:
- Information Technology
- The medicine
- Industry

Text: neurolink implants, combined with processing their data through machine learning, can become a new word in prosthetics
Selected field: Medicine, Information technology

Text: to make a chicken we need dough...
Selected area: none of the above, this is culinary

Text: James Webb telescope finally launched
Reference: The James Webb Space Telescope is an orbital infrared observatory. The largest space telescope with the largest mirror ever launched by mankind. Originally called the New Generation Space Telescope.
Selected area:

GPT3Bot
BOT
 — Today at 4:50 PM
Determine if the text belongs to one of the areas, if not - say how you would name its area.

Areas:
- Information Technology
- The medicine
- Industry

Text: neurolink implants, combined with processing their data through machine learning, can become a new word in prosthetics
Selected field: Medicine, Information technology

Text: to make a chicken we need dough...
Selected area: none of the above, this is culinary

Text: James Webb telescope finally launched
Reference: The James Webb Space Telescope is an orbital infrared observatory. The largest space telescope with the largest mirror ever launched by mankind. Originally called the New Generation Space Telescope.
Chosen field: astronomy
```

## Deployment
You should create `config.json` like next
```
{
    "cloudTranslation": {
        "account": {
            "type": "service_account",
            "project_id": "projectid",
            "private_key_id": "privatekeyid",
            "private_key": "privatekey",
            "client_email": "serviceemail",
            "client_id": "clientid",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "clientcert"
        },
        "parent": "projects/projectid"
    },
    "openAiKey": "openaikey",
    "discordToken": "discordtoken",
    "onErrorMessage": "The cortex chip does not response"
}
```
Than install libraries: `python -m pip install -r requirements.txt`
And run bot
```
$ python bot.py --config config.json
```