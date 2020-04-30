# -*- coding: utf-8 -*-
import telebot
import check
import process

token = "1084915585:AAFN6vrJlOEVzb6qXCekzSqEqbL8-mOQJ28"
bot = telebot.TeleBot(token)
owner = 231584958


@bot.message_handler(commands = ['all', 'start', 'help', 'donate', 'countmistakes', 'findmistakes', 'checkwords', 'checkcomma', 'checkshortcuts', 'countwords', 'all'])
def start_message(message):
    if message.text == "/start":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTv15eay4HLO9sIYOJPGwtDszOVh8TAAIFAAPANk8T-WpfmoJrTXUYBA')
        bot.send_message(message.chat.id, '''
Привет! Этот бот разработан студентом СТАНКИНА и посвящён людям, которые проверяют кучу эссе по английскому языку!
Он отметит часто встречающиеся ошибки в эссе (но не полагайся на него полностью, он далеко не идеален)

Надеюсь он сможет облегчить тебе жизнь!
Используй /help, чтобы узнать список команд!
''')
    elif message.text == "/help":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTxV5ea3654QNnjIkjhz4kp-t96vMvAAIYAAPANk8T1vonv5xqGPgYBA')
        bot.send_message(message.chat.id, '🛠 Доступные команды:')
        bot.send_message(message.chat.id, '''
---------------
/start
/help
/donate
---------------
/all
/countwords
/countmistakes
/checkwords
/checkcomma
/checkshortcuts
/findmistakes
---------------
''')

    elif message.text == "/donate":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTwl5eazLvO8AwsJVfiJhp1TQbHrIBAAITAAPANk8TqrOH9384yqUYBA')
        bot.send_message(message.chat.id, '''
Яндекс.Деньги: 410012188653567
Сбер: 5469380072221350
''')
        bot.send_message(owner, 'somebody pushed the /donate button')
        
    elif "/findmistakes" in message.text:
        if message.text == "/findmistakes":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /findmistakes text")
        else:
            if "олег" in (message.text).lower() or "макет" in (message.text).lower():
                bot.send_message(message.chat.id, "Сметане очень идет её цвет натуральный цвет кожи!!")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')
            text = message.text[14::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            responde = check.find_mistakes(text)
            bot.send_message(message.chat.id, responde)

    if "/countmistakes" in message.text:
        if message.text == "/countmistakes":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /countmistakes text")
        else:
            if "олег" in (message.text).lower() or "макет" in (message.text).lower():
                bot.send_message(message.chat.id, "Сметане очень идет её цвет натуральный цвет кожи!!")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')
            text = message.text[15::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            responde = process.count_mistakes(text)
            bot.send_message(message.chat.id, responde)

    elif "/checkwords" in message.text:
        if message.text == "/checkwords":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /checkwords text")
        else:
            if "олег" in (message.text).lower() or "макет" in (message.text).lower():
                bot.send_message(message.chat.id, "Сметане очень идет её цвет натуральный цвет кожи!!")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')
            text = message.text[12::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            responde = check.words(text)
            responde = process.array_to_string(responde)
            bot.send_message(message.chat.id, responde)

    elif "/checkcomma" in message.text:
        if message.text == "/checkcomma":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /checkcomma text")
        else:
            if "олег" in (message.text).lower() or "макет" in (message.text).lower():
                bot.send_message(message.chat.id, "Сметане очень идет её цвет натуральный цвет кожи!!")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')
            text = message.text[12::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            responde = check.comma(text)
            responde = process.array_to_string(responde)
            bot.send_message(message.chat.id, responde)

    elif "/checkshortcuts" in message.text:
        if message.text == "/checkshortcuts":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /checkshortcuts text")
        else:
            if "олег" in (message.text).lower() or "макет" in (message.text).lower():
                bot.send_message(message.chat.id, "Сметане очень идет её цвет натуральный цвет кожи!!")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')
            text = message.text[16::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            responde = check.shortcut(text)
            responde = process.array_to_string(responde)
            bot.send_message(message.chat.id, responde)

    elif "/countwords" in message.text:
        if message.text == "/countwords":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /countwords text")
        else:
            if "олег" in (message.text).lower() or "макет" in (message.text).lower():
                bot.send_message(message.chat.id, "Сметане очень идет её цвет натуральный цвет кожи!!")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')
            text = message.text[12::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            responde = process.array_to_string(process.count_words(text))
            bot.send_message(message.chat.id, responde)

    elif "/all" in message.text:
        if message.text == "/all":
            bot.reply_to(message, "Вставь текст, который хочешь проверить после комманды. Вот так: /all text")
        else:
            text = message.text[5::]
            bot.send_chat_action(message.chat.id, action = 'typing')
            text = check.find_mistakes(text)
            print(text)
            responde = text + process.count_mistakes(text)
            bot.send_message(message.chat.id, responde)


@bot.message_handler(content_types=['text'])
def troll_maria(message):
    if "олег" in (message.text).lower() or "макет" in (message.text).lower():
        bot.send_message(message.chat.id, "Сметане очень идет её натуральный цвет кожи!!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJTyF5evbloYBk_UiQfC1upRm14GXV3AAIZAAPANk8T0EOA9iBXFEsYBA')

bot.polling()