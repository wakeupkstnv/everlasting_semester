﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define dzh = Character('Джанкиева', color="#c8ffc8")
define bzb = Character('Базарбаева', color="#ff33f6")

# bg
image halyk_cowork = im.Scale("bg/kbtu_halyk_cowork.jpg", 1920, 1080)
image random_bg = im.Scale("More Images/school.png", 1920, 1080)


# dzhankieva character images
image closed_smile_girl = im.Scale("first girl/Summer Uniform/Aiko_SummerSera_Closed_Smile.png", 500, 950)
image closed_Smile_Blush = im.Scale("first girl/Summer Uniform/Aiko_SummerSera_Closed_Smile_Blush.png", 500, 950)
image SummerSera_Frown = im.Scale("first girl/Summer Uniform/Aiko_SummerSera_Frown.png", 500, 950)

# bazarbaeva character images
image saki_worried = im.Scale("second girl/saki/saki_worried.png", 900, 1450)

# Игра начинается здесь:
label start:

    show closed_smile_girl #at right
    with dissolve


    dzh "Привет Райымбек-Кун! Как дела?"

    hide closed_smile_girl
    show SummerSera_Frown
    with dissolve
    dzh "Ты выглядишь грустным..."

    hide SummerSera_Frown
    with dissolve
    u"???" "*Послышался шорох*"

    return