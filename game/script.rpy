# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define maximus = Character('55_maximus_55', color = "70E500")
define prepod1 = Character('Препод по Бесполезным вещам', color = "A60000")
define prepod2 = Character('Препод по Бессмысленным вещам', color = "A60000")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    $ day = 1
    $ day_end = 21

    $ cp_stage = 0
    $ labs_count = 0

    $ pred1 = False
    $ pred2 = False

    $ clothes = 0
    $ tea = False
    $ baltika = False

label start_day:
    if tea and baltika:
        "Нахуй смешивать чай с балтикой"
        jump game_over
    if day == day_end:
        jump game_over
    if pred1 and pred2:
        jump game_win
    $ tea = False
    $ baltika = False
    scene bg room morning
    if clothes == 0:
        show maximus normal
    if clothes == 1:
        show maximus winter
    maximus "Сегодня [day] число, меня отчислят [day_end] числа"

label start_day_menu:
    scene bg room morning
    if clothes == 0:
        show maximus normal
    if clothes == 1:
        show maximus winter
    menu:
        maximus "Что мне делать утром?"
        "Выпить чаю":
            scene bg tea
            "+ к работе над долгами"
            $ tea = True
            jump start_day_menu
        "Выпить балтику 9":
            scene bg baltika
            "+ к сдаче работ"
            $ baltika = True
            jump start_day_menu
        "Пойти в универ":
            jump day_sharaga
        "Делать долги":
            jump day_home
        "Переодеться":
            menu:
                "Пафосный":
                    $ clothes = 0
                "Зимний":
                    $ clothes = 1
            jump start_day_menu

label day_home:
    menu:
        "Какой долг мне делать?"
        "Курсовая работа: \"Теоретическое применение бесполезных вещей на практике\"":
            if tea:
                $ cp_stage += 1
                "Успешно сделан [cp_stage] пункт из 3"
            else:
                "Ничего не получается"
            jump day_evening
        "Лабораторные работы: \"Бессмысленные и беспощадные расчёты числа 42\"":
            if tea:
                $ labs_count += 1
                "Успешно сделана [labs_count] лаба из 4"
            else:
                "Ничего не получается"
            jump day_evening
    jump day_evening

label day_sharaga:
    scene bg sharaga
    if clothes == 0:
        show maximus normal
    if clothes == 1:
        show maximus winter
    menu:
        "Какой долг пытаться сдать"
        "\"Теоретическое применение бесполезных вещей на практике\"":
            if baltika and cp_stage == 3:
                prepod1 "Успешно сдан предмет"
                $ pred1 = True
            else:
                prepod1 "Хуйня, переделывай"
                $ cp_stage = 0
        "Лабораторные работы: \"Бессмысленные и беспощадные расчёты числа 42\"":
            if baltika and labs_count == 4:
                prepod2 "Успешно сдан предмет"
                $ pred2 = True
            else:
                prepod2 "Хуйня, переделывай"
                $ labs_count = 0
    jump day_evening


label day_evening:
    $ day += 1
    scene bg room evening
    if clothes == 0:
        show maximus normal
    if clothes == 1:
        show maximus winter
    maximus "Я устал, пойду спать"
    jump start_day

label game_over:
    maximus "Кому понадобилось с утра звонить?"
    maximus "Плохо, это с деканата"
    "Вы отчислены"
    "BAD END"
    return
label game_win:
    maximus "Я сдал долги"
    maximus "теперь меня не отчислят"
    "TRUE END"
    return
