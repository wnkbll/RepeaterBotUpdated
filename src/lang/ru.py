BOT: dict[str, str] = {
    "start": "Проверка пройдена.",
    "posts_number": "Текущее количество постов: {number}.",
    "add_post": "Отправьте новый пост.",
    "empty_list": "Список постов пустой.",
    "choose_post": "Выберите пост",
    "all": "Все",
    "post_edited": "Пост №{number} обновлён.",
    "send_edited": "Отправьте обновлённый пост.",
    "no_permissions": "У вас недостаточно прав.",
    "add_chat": "Отправьте новый чат.",
    "unexpected_args": "Вы ввели неправильные аргументы.",
    "bad_link": "Ссылка не обнаружена.",
    "bad_time": "Время не обнаружено.",
    "empty_chats": "Список чатов пустой.",
    "on_chat_edit": "Чат {chat} успешно изменён.",
    "on_sleep_edit": "Время сна успешно изменено.",
    "send_new_time": "Отправьте новое время.",
    "on_chat_remove": 'Чат `{link}` был успешно удалён.'
}

CLIENT: dict[str, str] = {
    "post_sent": "Сообщение в канал {title} отправлено."
}


def register(strings: dict) -> dict[str, dict[str, str]]:
    lang = "ru"
    strings[lang] = {}

    for item in BOT.items():
        strings[lang][item[0]] = item[1]

    for item in CLIENT.items():
        strings[lang][item[0]] = item[1]

    return strings
