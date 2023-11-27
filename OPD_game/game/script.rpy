# Определение персонажей игры.
define a = Character('Алекс', color = "#F5953D")
define n = Character('Неизвестный из монитора', color = "#808080")
define u = Character('Юрий Юлёрнович', color = "#366AF3")

# Игра начинается здесь:
label start:

    scene office

    show alex happy

    a " - Вот черт, опять программа зависла, 3 раз подряд, еще и кнопку отправки невозможно найти! Так работать невозможно."
    a " - Я ввел всего лишь террабайт информации, а ты, старая железка, не можешь ее обработать хотя бы в течение моей оставшейся жизни!!!"

    hide alex happy
    show alex happy reverse:
        xalign -0.1 yalign 1.3

    a " - Будь проклят тот день, когда я согласился работать в говнопрограмме с говнокодом."  
    a " - Если бы где-нибудь раздавали суперспособности, я бы выбрал способность понимать мышление компа, умение программировать и вообще бы стал крутым прогером!"

    hide alex happy reverse
    show alex happy:
        xalign -0.1 yalign 1.3
    show ulearnich happy:
        xalign 1.1 yalign 1.3

    n " - Хмм, могу устроить"

    hide ulearnich happy
    hide alex happy reverse
    show alex happy

    menu:
        "Так, все, пора завязывать с энергетиками, уже и голоса мерещатся":
            call Energos from _call_Energos
        "Похоже из-за того, что я не спал последние две ночи, пока бился над практическим заданием, у меня появились галлюцинации":
            call NeSpal from _call_NeSpal

    hide alex happy
    hide ulearnich happy
    show ulearnich happy:
        xalign 0.45 yalign 1.3

    u " - Я ТВОЙ ПОВЕЛИТЕЛЬ!!!"

    hide ulearnich happy
    hide alex happy

    show ulearnich happy:
        xalign 1.1 yalign 1.3
    show alex happy:
        xalign -0.1 yalign 1.3

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

    hide ulearnich happy
    hide alex happy
    show ulearnich happy:
        xalign 0.45 yalign 1.3

    u " - Выбор за тобой!"

    menu:
        "Блин, как-то стремно... Наверное, все же откажусь..":
            call Zassal from _call_Zassal
        "Ну и ладно, терять мне уже нечего, выберу синюю":
            call NeZassal from _call_NeZassal

    hide alex happy
    show alex happy:
        xalign 1.3 yalign 1.3
    show ulearnich happy reverse:
        xalign -0.1 yalign 1.3

    u " - ХАХАХА! Еще ни один не спросил, как вернуться обратно! Ну что ж, пока не поймет и не научится всему, так и будет скитаться по оптоволокну!"

    hide alex happy

    "Алекс дефрагментируется и залетает в монитор. Туда, откуда прибыл Юрий Юлёрнович"

    return
# Заканчивается тут.

label Energos:

    show alex happy:
        xalign -0.1 yalign 1.3
    show ulearnich happy:
        xalign 1.1 yalign 1.3

    n " - Ну допустим, не мерещится, а вот с энергетиками действительно заканчивай, вон глаза какие красные"
    menu:
        "Мне все это просто снится... просто снится..":
            call Snitsa from _call_Snitsa
            return
        "Что за??! Что происходит?":
            call ShoZa from _call_ShoZa
            return

label NeSpal:

    show alex happy:
        xalign -0.1 yalign 1.3
    show ulearnich happy:
        xalign 1.1 yalign 1.3

    n " - Эй, Алекс, Я вообще-то все еще здесь!"
    menu:
        "Что за??! Что происходит?":
            call ShoZa from _call_ShoZa_1
            return
        "Я же должен был остаться в офисе один...":
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
    hide ulearnich happy
    show alex happy reverse:
        xalign -0.1 yalign 1.3

    a " - Блин, как-то стремно... Наверное, все же откажусь.."

    hide alex happy reverse
    show alex happy:
        xalign -0.1 yalign 1.3
    show ulearnich happy:
        xalign 1.1 yalign 1.3

    u " - Вот ты душнила! Давай, вошли и вышли! Приключение на 20 минут!"

label NeZassal:
    hide ulearnich happy
    hide alex happy
    show alex happy

    a " - Ну и ладно, терять мне уже нечего, выберу синюю"
    return