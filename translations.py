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
  ["Select bot's language:", "Выберите язык бота:", "Виберіть мову бота:"], # 6 - language selection

  ["Oh shit, I'm sorry but problem occurred when track was downloading. Please try again",
   "Короче, как всегда что-то пошло не так. Не выбирай, пожалуйста, больше этот трек, так как мы понятия не имеем, что именно не работает",
  "Батько наш Бандера..."], # 7 - when exception occur before downloading (delete this)

  ["Switched to Stolen Music", "Поток перенаправлен в Stolen Music",
   "Потік перенапралений в Stolen Music"], # 8 - switching to Stolen Music

  ["Switched back to the Stolen Archive", "Поток вновь направлен в Stolen Archive",
   "Потік повернуто до Stolen Archive"], # 9 - switching to Stolen Archive

  ["Use /help to call this message again\nUse /search to find a song\nUse /lang to select bot's language\n" # 10 admins help
   "Use /switch to switch destination of tracks\nUse /group to see current destination of tracks",
   "Используйте /help чтобы увидеть это сообщение ещё раз\nИспользуйте /search для поиска песни\nИспользуйте /lang для выбора языка бота"
   "\nИспользуйте /switch что бы изменить группу для пересылки музыки\nИспользуйте /group что бы узнать куда пересылается музыка",
   "Відправте /help щоб побачити це повідомлення знову\nВідправте /search для пошуку пісні\nВідправте /lang для вибору мови бота\n"
   "Відправте /switch щоб змінити канал призначення музики\nВідправте /group щоб дізнатися канал в який надходить музика"],

    ["Stolen Archive", "RUS", "UKR"], # 11 /group -> Stolen Archive

    ["Stolen Music", "RUS", "UKR"] # 12 /group -> Stolen Music
]

UL = {}
