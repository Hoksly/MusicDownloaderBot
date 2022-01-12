LGS = ["English", "Русский", "Українська"]
CL = ["Bot's language switched to English", "Язык бота переключён на русский", "Мову бота змінено на українську"]
MT = [
  ["Hello!", "Привет!", "Привіт!"], # 0 - start
  ["Use /help to call this message again\nUse /search to find a song\nUse /lang to select bot's language",
   "Используйте /help чтобы увидеть это сообщение ещё раз\nИспользуйте /search для поиска песни\nИспользуйте /lang для выбора языка бота",
   "Відправте /help щоб побачити це повідомлення знову\nВідправте /search для пошуку пісні\nВідправте /lang для вибору мови бота"], # 1 - help
  ["Now send me a name of the song", "Теперь отправьте мне название песни", "Тепер відправте мені назву пісні"], # 2 - search
  ["Searching songs...", "Поиск песен...", "Пошук музики..."], # 3 - searching
  ["Search results:", "Результаты поиска:", "Результати пошуку:"], # 4 - results
  ["Sorry, couldn't find any songs with this name", "К сожалению, не удалось найти ни одной песни с таким названием", "На жаль, не вдалося знайти жодної пісні з такою назвою"], # 5 - not found
  ["Select bot's language:", "Выберите язык бота:", "Виберіть иову бота:"], # 6 - language selection
]
UL = {}

def main ():
  print ("!")
  # load UL from file
  # if program stops - save UL to file
