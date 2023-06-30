import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import *
from wikilist import *
from starwars import *




token = "vk1.a.bqMmUAS-DsSffBCz07C6z6BezHOfyUdQg9jmaCcQiutqszBq6vslqxTuvAq6bdxwthcrlDMvzGWF3bkAb8pgjYSr3KPlQDeMp55viIvmy3QbSPE1aorgH2_trXJ5tOJ9v9m7V0QMhf5CFjAFy6DNaICyIJUrkoBOT0h0XzE3_pejs-XETz8H8m1wv_xeSslmJ1dg0ja2VD-ijSyIfz85dw"

bot = vk_api.VkApi(token=token)
Vk = bot.get_api()
longpoll = VkLongPoll(vk=bot)



for event in longpoll.listen():
    #print(event.type)    
    if event.type == VkEventType.MESSAGE_NEW:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = event.message_id
        print(f"{user_id} {msg}")
        if msg == "курс":
            response = "{0} рублей за 1 доллар".format(get_course("R01235"))
            Vk.messages.send(user_id=user_id, random_id = random_id, message = response)
        elif msg[:3] == "вик":
            art = msg[3:]
            wikilist = get_wiki(art)
            Vk.messages.send(user_id=user_id, random_id = random_id, message = wikilist)

        elif msg == "планеты":
            response = get_planets_info()
            Vk.messages.send(user_id=user_id, random_id = random_id, message = response)

        elif msg == "корабли":
            response = get_starships_info()
            Vk.messages.send(user_id=user_id, random_id = random_id, message = response)

        elif msg == "valute":
            valute = ["usd", "eur"]
            usd = "Доллар"
            eur = "Евро"
            response = "{0} рублей за 1 valute".format(get_course())
            Vk.messages.send(user_id=user_id, random_id = random_id, message = response)


        #else:
            #Vk.messages.send(user_id=user_id, random_id = random_id, message ="Error")














































































































































































































































































"""import vk_api
from course import *

token = "vk1.a.bqMmUAS-DsSffBCz07C6z6BezHOfyUdQg9jmaCcQiutqszBq6vslqxTuvAq6bdxwthcrlDMvzGWF3bkAb8pgjYSr3KPlQDeMp55viIvmy3QbSPE1aorgH2_trXJ5tOJ9v9m7V0QMhf5CFjAFy6DNaICyIJUrkoBOT0h0XzE3_pejs-XETz8H8m1wv_xeSslmJ1dg0ja2VD-ijSyIfz85dw"

bot = vk_api.VkApi(token=token)

messages = bot.method("messages.getConversations", {"count": 20, "filter": "unanswered"})

while True:
    messages = bot.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        print(messages)
        user_id = messages["items"][0]["last_message"]["from_id"]
        message_id = messages["items"][0]["last_message"]["id"]
        message_text = messages["items"][0]["last_message"]["text"]
        if message_text.lower() == "курс":
            bot.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message": get_course("R01235")})
        else:
            bot.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message":  "неизвестная команда"})
            """


