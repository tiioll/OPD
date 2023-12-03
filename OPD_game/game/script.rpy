﻿# Определение персонажей игры.
define a = Character('Алекс', color = "#F5953D")
define n = Character('Неизвестный из монитора', color = "#BBBBBB")
define u = Character('Юрий Юлёрнович', color = "#366AF3")

init:
    $ DedRight = Position(xalign = 1.1, yalign = -1.5)

    $ AlexLeft = Position(xalign = 0.0, yalign = 0.8)
    $ AlexCenter = Position(xalign = 0.3, yalign = 0.8)

# Игра начинается здесь:
label start:

    scene office

    show alex:
        xalign 0.3 yalign 0.8

    a " - Вот черт, опять программа зависла, 3 раз подряд, еще и кнопку отправки невозможно найти! Так работать невозможно."
    a " - Я ввел всего лишь террабайт информации, а ты, старая железка, не можешь ее обработать хотя бы в течение моей оставшейся жизни!!!"

    hide alex
    show alex at AlexLeft

    a " - Будь проклят тот день, когда я согласился работать в говнопрограмме с говнокодом."  
    a " - Если бы где-нибудь раздавали суперспособности, я бы выбрал способность понимать мышление компа, умение программировать и вообще бы стал крутым прогером!"

    hide alex
    show alex at AlexLeft
    show ulearnich at DedRight

    n " - Хмм, могу устроить"

    hide ulearnich
    hide alex
    show alex at AlexCenter

    menu:
        " - Так, все, пора завязывать с энергетиками, уже и голоса мерещатся":
            call Energos from _call_Energos
        " - Похоже из-за того, что я не спал последние две ночи, пока бился над практическим заданием, у меня появились галлюцинации":
            call NeSpal from _call_NeSpal

    hide alex
    hide ulearnich
    show ulearnich

    u " - Я ТВОЙ ПОВЕЛИТЕЛЬ!!!"

    hide ulearnich
    hide alex

    show ulearnich at DedRight
    show alex at AlexLeft

    u " - Ладно, шутка! Не парься так, я на самом деле добрый бог программирования."

    a " - Но,но... как ты здесь очутился??"

    u " - По сети BLUETOOTH прилетел АХАХАХА!"
    u " - Ладно, как я сказал ранее, я - божество, олицетворяющее идеального программиста. Я могу переместиться в любую точку земного шара по щелчку пальца!"
    u " - Вот недавно, например, Маска навещал. Помогал ему запуски ракет рассчитывать. Но потом мне все это надоело, и вот, я болтаю тут с тобой"
    u " - Что-то заболтался я..."
    u " - Ну так что? Помочь тебе разобраться в этом бездонном мире нулей и единиц? Хочешь научиться программировать?  Оптимизировать сайты?  Зарабатывать кучу денег и жить на Майами?"
    
    a " - Конечно, хочу! Я бы многие программы и сайты оптимизировал, сил больше моих нет, тут сидеть и ждать, пока все заработает. Что нужно делать?"
    
    u " - Короче, все по классике, выбери синюю или красную!  "
    u " - Я догадываюсь, что ты сейчас ощущаешь себя словно Алиса, падающая в кроличью нору"
    u " - Выберешь красную - так и останешься постепенно лысеющим сисадмином на скучной работе"
    u " - Выберешь синюю - узнаешь, насколько глубоки строение и архитектура программ"

    hide ulearnich
    hide alex
    show ulearnich

    u " - Выбор за тобой!"

    hide ulearnich
    hide alex
    show alex at AlexCenter

    menu:
        "Отказаться":
            call Zassal from _call_Zassal
        "Согласиться":
            call NeZassal from _call_NeZassal

    hide alex
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - ХАХАХА! Еще ни один не спросил, как вернуться обратно! Ну что ж, пока не поймет и не научится всему, так и будет скитаться по оптоволокну!"

    hide alex

    "Алекс дефрагментируется и залетает в монитор. Туда, откуда прибыл Юрий Юлёрнович."

    scene code

    show alex at AlexCenter

    a " - Я лечуууууу!?! Крутоооо! Как в детстве во сне))"

    hide alex
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - Эй, эй! Аккуратней с воспоминаниями, смотри, чтоб как в детстве не оконфузился..."
    a " - ха-ха, очень смешно"
    a " - Да ну тебя! Где мы? Что со мной?"
    u " - Сейчас мы с тобой пучки электронов, летим по оптоволокну, где то  посреди компьютера. Ну так что?! Не забыл для чего мы здесь?"
    u " - Чему хочешь для начала научиться? Блокчейн? Настройка мозговых имплантов? Сенсорика? Дополненная реальность?"

    menu:
        " - Даже не знаю, мне надо подумать":
            call Podumat
        " - Хмм, половину слов не понял, А есть что- нибудь для начала совсем уж простое?":
            call Zatichka

    return
# Заканчивается тут.

label Energos:

    show alex at AlexLeft
    show ulearnich at DedRight

    n " - Ну допустим, не мерещится, а вот с энергетиками действительно заканчивай, вон глаза какие красные"
    menu:
        " - Мне все это просто снится... просто снится..":
            call Snitsa from _call_Snitsa
            return
        " - Что за??! Что происходит?":
            call ShoZa from _call_ShoZa
            return

label NeSpal:

    show alex at AlexLeft
    show ulearnich at DedRight

    n " - Эй, Алекс, Я вообще-то все еще здесь!"
    menu:
        " - Что за??! Что происходит?":
            call ShoZa from _call_ShoZa_1
            return
        " - Я же должен был остаться в офисе один...":
            call Odin from _call_Odin
            return 


label Snitsa:
    n " - Переставай нудить парень, я практически также реален как и ты"
    a " - Но..но... кто со мной общается сейчас? Кто ты или что ты такое?!?"
    return

label ShoZa:
    a " - Наверное, просто глупый розыгрыш"
    n " - Да кому ты нужен, разыгрывать тебя, сидишь тут штаны просиживаешь!"
    a " - Но..но... кто со мной общается сейчас? Кто ты или что ты такое?!?"
    return

label Odin:
    a " - Но..но... кто со мной общается сейчас? Кто ты или что ты такое?!?"
    return

label Zassal:
    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich at DedRight

    a " - Блин, как-то стремно... Наверное, все же откажусь.."

    u " - Вот ты душнила! Давай, вошли и вышли! Приключение на 20 минут!"

label NeZassal:
    hide ulearnich
    hide alex
    show alex at AlexLeft
    show ulearnich at DedRight

    a " - Ну и ладно, терять мне уже нечего, выберу синюю"
    return

label Podumat:


label Zatichka:
