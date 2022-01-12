LGS = ["English", "Русский", "Українська"]
UL = {}
MT = [
  ["Hello!", "Привет!", "Привіт!"], # 0 - start
  ["Use /help to call this message again\nUse /search to find a song\nUse /lang to select bot's language",
   "Используй /help чтобы увидеть это сообщение ещё раз\nИспользуй /search для поиска песни\nИспользуй /lang для выбора языка бота",
   "Відправ /help щоб побачити це повідомлення знову\nВідправ /search для пошуку пісні\nВідправ /lang для вибору мови бота"], # 1 - help
  ["Now send me a name of the song", "Теперь отправь мне название песни", "Тепер відправ мені назву пісні"] # 2 - search
]

def main ():
  print ("!")
  # load UL from file
  # if program stops - save UL to file
