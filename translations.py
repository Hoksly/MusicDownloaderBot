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

  ["It looks like something went wrong. Please, try again. If this message persists, contact with @Hoksly or @Cubatomic",
   "Похоже, что-то пошло не так. Пожалуйста, попробуйте снова. Если это сообщение продолжит появляться, свяжитесь с @Hoksly или @Cubatomic",
  "Здається, сталося щось неочікуване. Будь ласка, спробуйте знову. Якщо це повідомлення продовжить з\'являтись, повідомте про це @Hoksly або @Cubatomic"], # 7 - something went wrong

  ["Use /help to call this message again\nUse /search to find a song\nUse /lang to select bot's language\n" # 8 - admin help
   "Use /switch to switch destination of tracks\nUse /group to see current destination of tracks",
   "Используйте /help чтобы увидеть это сообщение ещё раз\nИспользуйте /search для поиска песни\nИспользуйте /lang для выбора языка бота"
   "\nИспользуйте /switch что бы изменить группу для пересылки музыки\nИспользуйте /group что бы узнать куда пересылается музыка",
   "Відправте /help щоб побачити це повідомлення знову\nВідправте /search для пошуку пісні\nВідправте /lang для вибору мови бота\n"
   "Відправте /switch щоб змінити канал призначення музики\nВідправте /group щоб дізнатися канал в який надходить музика"],
    ["Current forwarding chat: ", "Текущая чат для пересылки: ", "Поточний чат для пересилання: "], # 9 - current group
    ["Choose forwarding group: ", "Выберите группу для пересылки: ", "Виберіть чат для пересилання: "] # 10 - switch group choose
    ["Forwarding chat changed to ", "Чат для пересылки изменён на ", "Чат для пересилання змінено на "] # 11 - switch group
]

UL = {}
