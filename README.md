<h1 align="center"> FunPay bot</h1>
<h4 align="center">Консольное приложение для автоматизации рутинных действий на FunPay</h4>

## :clipboard: **Содержание**

- [Возможности](#robot-возможности)
  - [FunPay](#shopping_cart-funpay)
  - [Уведомления в Telegram](#left_speech_bubble-уведомления-в-telegram)
  - [Дополнительные возможности](#gear-дополнительные-возможности)

- [Преимущества](#1st_place_medal-преимущества)
  - [Для пользователей](#grinning-для-пользователей)
  - [Для разработчиков](#computer-для-разработчиков)

- [Установка](#robot-установка)
  - [Windows](#window-windows) 
- [Настройка конфигов](#hammer_and_wrench-настройка-конфигов)
- [Установка плагинов](#electric_plug-установка-плагинов)

------------------------------------------
## :robot: **Возможности**

### :shopping_cart: **FunPay**

- Авто-выдача товаров.
- Авто-поднятие лотов.
- Авто-ответ на заготовленные команды.
- Авто-восстановление лотов после продажи.
- Вечный онлайн.
- Уведомления в телеграм.
-----------------------------
### :left_speech_bubble: **Уведомления в Telegram**

- Возможность установки нескольких чатов для уведомлений.
- Уведомления о поднятии лотов.
- Уведомления о новых заказах.
- Уведомления о выдаче товара.
- Уведомления о новых сообщениях
- Возможность отвечать на сообщения прямо из Telegram.
------------------------------------------
### :gear: **Дополнительные возможности**

- Использование переменных в тексте для авто-ответа / авто-выдачи.
- Создание плагинов для кастомизации функционала без редактирования исходного кода самого Кардинала.
------------------------------------------
## :1st_place_medal: **Преимущества**

### :grinning: **Для пользователей**

- **Больше**, чем наличие самого нужного функционала.
- **Оптимизация**. _20 МБ свободного места на диске, до 50 МБ ОЗУ, доступ в интернет_ - все что нужно для работы.
- Возможность установить на **любую платформу**, которую поддерживает _Python: Windows, Linux, IOS, Android_ и т.д.
- Возможность установки плагинов дает **огромную вариативность** модификации стандартного функционала под самые разные нужды.
- Гибкие и при этом простые конфиги, написанные в INI-формате.
- Постоянные обновления, быстрое реагирования на баги / предложения о новом функционале.
------------------------------------------
### :computer: **Для разработчиков**

- Выбран самый простой и при этом один из самых мощных языков для такого рода приложений - _Python_.
- Полная документация кода. Все классы / методы / функции имеют док-строки, type-хинты.
- Широкое использование ООП. Почти каждый эвент / сообщение / заказ и т.д. представляют собой экземпляр соответствующего класса, а не просто набор данных в JSON.
- Возможность легкого создания плагинов.
- Сконфигурированный логгер. Никаких принтов!
- Собственный Python-пакет FunPayAPI, который никак не привязан к FunPay Cardinal.
- Поддержка лично от меня :)
------------------------------------------
## :robot: Установка 

### :window: Windows

1. Скачиваем Python `https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe`.
2. Запускаем установщик и снизу ставим галочку на `Add Python PATCH`.
3. После нажимаем на установить и ждём установки (в конце не нажимаем на `Disable` а просто закрываем установщик).
4. Скачиваем архив `https://github.com/Beesc9it/FunPay-bot`.
5. Распаковываем его в любую папку.
6. Запускаем в данной папке `installer_pack.bat` он установит вам нужные пакеты.

   Если не сработало то пробуем ручками от `6.1` до `6.2`)))
   
   6.1 Открываем `cmd` и вписываем путь до папки `cd путь до папки` если у вас другой диск то вписываем название диска пример: `d:` и опять указываем путь.

   6.2 Вводим команду `python3.11 setup.py` или `py setup.py` для установки нужных пакетов.
   

7. Заходим в папку `configs` и в `_main.cfg`

   7.1 Указываем следующие - в [FunPay] `golden_key`, `user_agent`
   
   Расширение для получения `golden_key голден кей получаем на сайте funpay` (НУЖНО БЫТЬ АВТОРИЗОВАННЫМ НА САЙТЕ):
   
       https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=ru

    Ваш юзер агент можно получить тут: `https://whatmyuseragent.com/` (нажмите на `copy`)

   7.2 Указываем - в [Telegram] `token`, `secretKey`
   
        Бот для тг создаем в `https://t.me/BotFather` и получаем токен бота
  (формат пример: `3476237846:lifgdusho8UGHF3ru8i4ygh4iughvewhgewt` - полностью!!!)
  
        `secretKey` - это тайный пароль который позволит использовать бота только вам
          (нужно будет ввести при первом запуске бота)
   
   8. Запускаем бота через `start.bat`
------------------------------------------
## :hammer_and_wrench: Настройка конфигов

1. Все конфиги находятся в папке `configs`
2. Все инструкции по настройке конфигов находятся внутри самих конфигов.
3. Основной конфиг со всеми переключателями: `configs/_main.cfg`
4. Конфиг авто-ответчика: `configs/auto_response.cfg`
5. Конфиг авто-выдачи: `configs/auto_delivery.cfg`
------------------------------------------
## :electric_plug: Установка плагинов
Установка плагинов крайне проста. Просто скопируйте файл плагина (с расширением `.py`) в папку `plugins`.
"# FunPay-bot-" 
"# FunPay-bot-" 
