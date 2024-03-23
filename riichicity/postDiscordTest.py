import requests
import json


def post_discord_test(message: str):
    original_webhook_url = "https://discord.com/api/webhooks/1215928991190614079/cmDGIE-AVqkh__hEcE3v4KSctgG2b7RlZi35weHuxAnCd4073sH_vpF2_2catQY95DLj"
    toukei_webhook_url = "https://discord.com/api/webhooks/1220997658735411201/LaNlTXZ0_jWmKvt-mxblQ_L-u5lik54jtsSnT5_v5nKoFBPr00wVkBb5cI5bv5ekKgyW"
    sanma_en_ton_webhook_url = "https://discord.com/api/webhooks/1220998671408304180/C1Z0RVKJclhnKCJIrCQtn9ceLqL1K6OCMa9Mt1wpqA9M78siBIno_cLUx4DNUZPKx30Y"
    sanma_en_han_webhook_url = "https://discord.com/api/webhooks/1220999122707025970/Nx9CeMTAU_W654vzyzZkueeuZrFAADvPEOq6y5bo0cXhr_-oU9b7HI8H2LMaWoNOOZlC"
    sanma_gin_ton_webhook_url = "https://discord.com/api/webhooks/1220999131548356658/N6nFPI-IwopykNxsa5zzUVqMvXO2a8TksV9nswpEbI1YMjmW1IEd-2R5yCI2mE7cltgS"
    sanma_gin_han_webhook_url = "https://discord.com/api/webhooks/1220999594180345897/LgO4JvgnVvdCktwQSN13nA5tSfFp87XMU-2bPYyUbQmqrQ9Sg-t9LFDx-JIYcAYnM8ly"
    yonma_gin_han_webhook_url = "https://discord.com/api/webhooks/1221001516471812127/HhPLAznx8t273Loza4tirEL9h9mbU8G2BYsX1jH_MwJq-71pTio937JXME3pd0yyZFSJ"
    yonma_gin_ton_webhook_url = "https://discord.com/api/webhooks/1221001742184091689/HJn9nmfpwegYdtlGNtyp-TI3hMNCNhVM3vCE1cDyhBiX7_MzhhVfBEjTloMj9UHb5_EZ"
    yonma_en_han_webhook_url = "https://discord.com/api/webhooks/1221002016965263391/cRzh8YaToJfXFAj3TuAtlLg-yG6iGDvHgJPi0-id9gSemakQy3p6PCoQnds8kP0hZcEG"
    yonma_en_ton_webhook_url = "https://discord.com/api/webhooks/1221002204710703114/ytj_od2O5PjO13baJpDffAIAsrxPrCJAlELSiBQkV3poEE5gbjESksEiq0m9QDQ1iKo8"
    urls = [original_webhook_url, toukei_webhook_url, sanma_en_ton_webhook_url, sanma_en_han_webhook_url, sanma_gin_ton_webhook_url, sanma_gin_han_webhook_url, yonma_gin_han_webhook_url, yonma_gin_ton_webhook_url, yonma_en_han_webhook_url, yonma_en_ton_webhook_url]
    for url in urls:
        messagejson = {"content": message}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, data=json.dumps(messagejson), headers=headers)
        print(response.text)


post_discord_test("モーニングカナちゃんだよ〜！")