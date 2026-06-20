import random
import telebot

bot = telebot.TeleBot("8808468688:AAHZeZ5oEJYECnyoSYTMgWOwVjIZmksJrs4")

@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет, я бот помощник в экологии")

@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.send_message(message.chat.id, """Список команд:\n
    /rand_fact - Бот даст рандомный факт\n
    /rules - правила
    """)           

@bot.message_handler(commands=["rand_fact"])
def facts_bot(message):
    facts = ["Слово «экология» происходит от древнегреческого языка и переводится как «наука о доме, жилище", "Около 12% поверхности Земли имеют заповедный статус", "Одна пластиковая бутылка разлагается около 450 лет.", "Кошки истребили минимум 30 видов животных.", "Лишь 1% пресной воды доступен для использования.", "Тысячи человек ежегодно умирают из-за плохого качества воды.", "Лишь 1% пресной воды доступен для использования", "Озоновый слой восстанавливается благодаря запрету на использование хлорфторуглеродов, который был закреплён в Монреальском протоколе (1987 год)", "За последние полвека количество пресной воды на каждого жителя планеты сократилось примерно на 60%"]
    bot.send_message(message.chat.id, random.choice(facts))

@bot.message_handler(commands=["rules"])
def rules_bot(message):
    bot.send_message(message.chat.id, """Правила:\n
    1. Беречь воду.\n
    2. Сортировать мусор.\n
    3. Экономить электроэнергию.\n
    4. Уважительно относиться к природе.\n
    5. Помогать животным и растениям.\n                 
    6. Беречь бумагу.\n
    7. Не мусорить.\n
    8. Выбирать экологичные альтернативы.
    """)          

bot.polling()      

