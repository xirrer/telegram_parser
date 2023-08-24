# telegram_parser
This programm can parse telegram channels and chats 

Этот код предназначен для извлечения сообщений и информации об участниках из каналов и чатов Telegram с использованием библиотеки Telethon. Код состоит из трех основных функций:
`dump_all_messages(channel)`: Извлекает все сообщения из указанного канала или чата и сохраняет их в файл `channel_messages.json`.
`dump_all_participants(channel)`: Извлекает информацию обо всех участниках указанного канала или чата и сохраняет их в файл `channel_users.json`.
`main()`: Основная функция, которая запрашивает у пользователя ссылку на канал или чат и вызывает функцию `dump_all_messages(channel)`.

# инструкция по использованию
Установите библиотеку Telethon, если у вас ее еще нет:
`pip install telethon`

Создайте файл `config.ini` в той же директории, где находится код. В файле должны быть следующие параметры:
```
[Telegram]
api_id = ВАШ_API_ID
api_hash = ВАШ_API_HASH
username = ВАШ_ЛОГИН
```
Замените `ВАШ_API_ID`, `ВАШ_API_HASH` и `ВАШ_ЛОГИН` на соответствующие значения, полученные при регистрации вашего приложения на `my.telegram.org`.
Запустите код. Вам будет предложено ввести ссылку на канал или чат. Введите ссылку и нажмите Enter.
После завершения работы кода, вы найдете два файла в той же директории: `channel_messages.json` и `channel_users.json`. В первом файле будут содержаться все сообщения из канала или чата, а во втором - информация об участниках.
