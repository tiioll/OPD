# Определение персонажей игры.
define a = Character('[Alex]', color = "#25dbef")
define n = Character('Неизвестный из монитора', color = "#BBBBBB")
define u = Character('Юрий Юлёрнович', color = "#366AF3")
define autor = Character("Голос в голове", color = "#BBBBBB")

define audio.ded_spawn = "audio/spawn_ded.mp3"
define audio.into_pc = "audio/into_pc.mp3"
define audio.minigame_music = "audio/minigame_music.mp3"
define audio.final = "audio/final.mp3"

init:
    $ DedRight = Position(xalign = 1.0, yalign = -1.5)

    $ AlexLeft = Position(xalign = 0.0, yalign = -0.5)
    $ center = Position(xalign = 0.5, yalign = -0.5)

# Игра начинается здесь:
label start:

    scene office

    show alex at center

    $ Alex = renpy.input("Введите имя персонажа", length=14)

    hide alex
    show alex a at center

    a " - Вот черт, опять программа зависла!"
    a " - Это уже 3 раз подряд!"
    a " - Еще и кнопку отправки невозможно найти!"
    a " - Так работать невозможно."
    a " - Я ввел всего лишь террабайт информации, а ты, старая железка, не можешь ее обработать хотя бы в течение моей оставшейся жизни!!!"
    a " - Будь проклят тот день, когда я согласился работать в говнопрограмме с говнокодом."  
    a " - Если бы где-нибудь раздавали суперспособности, я бы выбрал способность понимать мышление компа, умение программировать и вообще бы стал крутым прогером!"

    hide alex
    show alex at AlexLeft
    show ulearnich h at DedRight

    play sound ded_spawn

    n " - Хмм, могу устроить"

    hide ulearnich
    hide alex
    show alex at center

    menu:
        " - Так, все, пора завязывать с энергетиками, уже и голоса мерещатся":
            call Energos from _call_Energos
        " - Похоже из-за того, что я не спал последние две ночи, пока бился над проектом, у меня появились галлюцинации":
            call NeSpal from _call_NeSpal

    hide alex
    hide ulearnich
    show ulearnich

    u " - Я ТВОЙ ПОВЕЛИТЕЛЬ!!!"

    hide ulearnich
    hide alex

    show ulearnich h at DedRight
    show alex at AlexLeft

    u " - Ладно, шутка! Не парься так, я на самом деле добрый бог программирования."

    hide ulearnich
    show ulearnich at DedRight

    a " - Но,но... как ты здесь очутился?"

    hide ulearnich
    show ulearnich h at DedRight

    u " - По сети BLUETOOTH прилетел АХАХАХА!"

    hide ulearnich
    show ulearnich at DedRight

    u " - Ладно, как я сказал ранее, я - божество, олицетворяющее идеального программиста. Я могу переместиться в любую точку земного шара по щелчку пальца!"
    u " - Вот недавно, например, Маска навещал. Помогал ему запуски ракет рассчитывать. Но потом мне все это надоело, и вот, теперь я здесь"
    u " - Что-то заболтался я..."
    u " - Ну так что? Помочь тебе разобраться в этом бездонном мире нулей и единиц? Хочешь научиться кодить?  Оптимизировать программы?  Зарабатывать кучу денег и жить на Майами?"
    
    hide alex
    show alex h at AlexLeft

    a " - Конечно, хочу! Я бы многие программы и сайты оптимизировал, сил больше моих нет, тут сидеть и ждать, пока все заработает. Что нужно делать?"
    
    hide alex
    show alex at AlexLeft

    u " - Короче, все по классике, выбери синюю или красную!"
    u " - Я догадываюсь, что ты сейчас ощущаешь себя словно Алиса, падающая в кроличью нору"
    u " - Выберешь красную - так и останешься постепенно лысеющим сисадмином на скучной работе"
    u " - Выберешь синюю - узнаешь, насколько глубоки строение и архитектура программ"

    hide ulearnich
    hide alex
    show ulearnich

    u " - Выбор за тобой!"

    hide ulearnich
    hide alex
    show alex at center

    menu:
        "Отказаться":
            call Zassal from _call_Zassal
        "Согласиться":
            call NeZassal from _call_NeZassal

    hide alex
    show alex at AlexLeft
    show ulearnich h at DedRight

    u " - ХАХАХА! Еще ни один не спросил, как вернуться обратно! Ну что ж, пока не поймет и не научится всему, так и будет скитаться по оптоволокну!"

    hide alex

    autor "[Alex] дефрагментируется и залетает в монитор. Туда, откуда прибыл Юрий Юлёрнович."

    #SCENA 2

    scene intopc

    show alex h at center

    play sound into_pc

    a " - Я лечу-у-у-у?! Круто-о-о-о! Как в детстве во сне-е-е-е))"

    hide alex
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - Эй, эй! Аккуратней с воспоминаниями, смотри, чтоб как в детстве не оконфузился..."

    hide alex
    show alex a at AlexLeft

    a " - Ха-ха, очень смешно"

    hide alex
    show alex at AlexLeft

    a " - Да ну тебя! Где мы? Что со мной?"
    u " - Сейчас мы с тобой пучки электронов, летим по оптоволокну, где то посреди компьютера. Ну так что?! Не забыл для чего мы здесь?"
    u " - Чему хочешь для начала научиться? Блокчейн? Настройка мозговых имплантов? Сенсорика? Дополненная реальность?"
    
    hide ulearnich
    hide alex
    show alex at center

    menu:
        " - Даже не знаю, мне надо подумать":
            call Podumat from _call_Podumat
        " - Хмм, половину слов не понял, А есть что- нибудь для начала совсем уж простое?":
            call Zatichka from _call_Zatichka
    
    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - Дай ка подумать... вот, вспомнил! видел я тут по пути один сайт"
    u " - Автор его заслуженный оператор ЭВМ с госнаградой СССР «Золотая перфокарта» - Зинаида Петровна Лавлейс, дальний родственник легендарной Ады Лавлейс"
    
    hide alex
    hide ulearnich
    show alex at center

    menu:
        " - Кто? впервые слышу про них.":
            call Lekciya from _call_Lekciya
        " - Звучит круто, но я в теме. А что с сайтом не так?":
            call Zatichka from _call_Zatichka_1

    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich at DedRight

    u ' - Да понимаешь, Зинаида Петровна долгое время проработала в закрытом НИИ'
    u ' - Сайт делала уже будучи на пенсии в 90х годах и возможно по старой привычке создала нечто, больше походящее на оружие массового психоза, чем на сайт'
    u ' - Неокрепшим современным умам на такое смотреть не рекомендуется. В интернете и так полно сумасшедших, зачем их плодить еще больше.'
    u ' - Короче, вот тебе сайт. Тебе нужно обезвредить его путем ликвидации кривой графики.'

    hide alex
    show alex h at AlexLeft

    a ' - Звучит круто, я готов, сэнсэй!'

    hide ulearnich
    show ulearnich h at DedRight

    u ' - Хаха, а ты мне уже начинаешь нравиться. Вперед! Рассудок не потеряешь, перейдем к чему нибудь посложнее.'
    
    hide alex
    hide ulearnich

    call MiniGame1 from _call_MiniGame1

    #SCENA 3

    scene intopc

    show alex h at AlexLeft
    show ulearnich at DedRight

    play sound into_pc

    u ' - Иииииии ПОЗДРАВЛЯЮ! Первое задание выполнено!'
    u ' - Я бы конечно справился чуть быстрее, скажем раз в сто, но для кожаного мешка вполне себе не плохо! Как себя чувствуешь? Помнишь еще кто ты, и зачем ты здесь?'

    hide alex
    hide ulearnich
    show alex h at center

    menu:
        " - Оо да, теперь я готов к чему угодно":
            call Zatichka from _call_Zatichka_2
        " - Фууууф, помню конечно, было тяжело, но очень интересно. Чувствую себя рыцарем свежего, убрал весь мусор с сайта.":
            call Zatichka from _call_Zatichka_3

    hide alex
    hide ulearnich
    show alex a at AlexLeft
    show ulearnich h at DedRight

    u ' - Хе хе, очистил один давно забытый сайт и чувствуешь себя героем?! А как же остальные примерно 100\% сайтов мира?!'

    hide ulearnich
    show ulearnich at DedRight
    hide alex
    show alex at AlexLeft

    u ' - Ну ладно, это уж потом как нибудь сам, если захочешь. Работаем дальше?'
    a ' - Да, конечно, я готов продолжать'
    u ' - Хех, согласился он, как-будто у него есть выбор...'
    u ' - Ну ладно, что у нас дальше?'
    u ' - Визуально ты научился работать, давай попробуем копнуть глубже. Полетели, знаю я тут одну прогу, поковыряемся в ее коде'
    
    hide alex
    hide ulearnich
    show alex at center

    menu:
        " - Ох блин, я еще плохо программирую, может все таки продолжим сайты чистить?":
            call Chistit from _call_Chistit
        " - Ухх, я заряжен, погнали!":
            call Zatichka from _call_Zatichka_4

    scene code

    show alex h at AlexLeft
    show ulearnich at DedRight

    play sound into_pc

    a ' - Ого! Прямо как в фильме, вокруг падающие знаки и элементы кода!'

    hide ulearnich
    show ulearnich h at DedRight

    u ' - Ага! Я там, кстати, на заднем фоне снялся в эпизодической роли гениальной строчки кода. Но ее заметили только профи'

    hide ulearnich
    show ulearnich at DedRight
    hide alex
    show alex at AlexLeft

    u ' - Короче! Слушай мою команду! Мы внутри кода, код скажем так, слегка попахивает, да что там, от него разит! ничего не оптимизировано, все лагает, ссылки цикличны, множество повторов'
    u ' - В общем, ситуацию надо исправлять'

    hide alex
    hide ulearnich
    show alex at center

    menu:
        " - Ладно, за работу!":
            call Zatichka from _call_Zatichka_5
        " - Да вроде все норм, чет не вижу":
            call DaVrodeNorm from _call_DaVrodeNorm

    call MiniGame2 from _call_MiniGame2


    

    scene code4

    hide alex
    hide ulearnich
    show alex a at AlexLeft
    show ulearnich h at DedRight

    play sound into_pc

    u " - Хм, а ты не такой уж и бездарь, каким казался вначале. Надо же, справился с последней задачей."

    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - Как сказал один боксер: «А сегодня в оптимизацию не все могут. Вернее могут не только лишь все, мало кто может это!»"
    u " - Золотые слова!"
    u " - И запомни: «Тестировщик не выдаст, заказчик не съест!»"
    a " - Ничего не понял, но очень интересно"

    hide ulearnich
    show ulearnich h at DedRight
    hide alex
    show alex a at AlexLeft

    u " - Потом поймешь, неуч"

    #Konec 3 glavi

    $'''

    scene intopc

    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - Ну что мой юнный подаван, ты готов к финальному испытанию?"

    hide alex
    show alex at AlexLeft

    a " - Конечно, после предыдущих испытаний мне ничего не страшно, я готов на все!"

    hide ulearnich
    show ulearnich h at DedRight

    u " - Правда?) займи тогда пару лямов на стартап"

    hide alex
    show alex a at AlexLeft

    a " - Очень смешно. Не на столько на всё! Давай свое испытание"

    hide ulearnich
    show ulearnich at DedRight
    hide alex
    show alex at AlexLeft

    u " - Ладно! Как говорили Стругацкие «Нет на свете ничего такого, чего нельзя было бы исправить»"
    u " - Перед нами железо, да не простое, компьютерное! С компонентами!"
    u " - Да только собрано оно руками что из заднего места растут, оборвать бы их кому-то"
    u " - Можно придумать оптимизированную реализацию, спроектировать удобный сайт и сделать кучу всего, если знаешь устройство компа! В противном случае, все это нереально!"
    u " - Трудновато, знаешь ли, на не включаемом или зависшем компе творить великое и вечное!"
    a " - Согласен! Никогда не ковырялся в железе, но готов попробовать"
    u " - Так вперед, пофиксь все ошибки!"

    call MiniGame3 from _call_MiniGame3

    $'''

    scene intopc

    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich at DedRight

    u " - Что ж, могу тебя поздравить! Ты прошел все испытания! Надеюсь, теперь ты не будешь вымещать зло на компьютере или программном обеспечении!"
    u " - Все дело только в тебе! Учись, развивайся! Человек сам творец своего счастья!"
    
    hide alex
    show alex h at AlexLeft

    a " - Спасибо тебе! Я запомню все, что со мной тут было на всю жизнь!"

    hide ulearnich
    show ulearnich h at DedRight

    u " - Да ладно тебе, давай, вали уже в свой реальный мир"
    
    play sound final

    hide alex
    hide ulearnich
    show ulearnich

    u " - ХАХАХАХАХА, [Alex], ты же не думаешь, что на этом все закончилось?)"
    u " - Игра только началась!"

    return
# Заканчивается тут.

label Energos:

    show alex at AlexLeft
    show ulearnich a at DedRight

    n " - Ну, допустим, не мерещится, а вот с энергетиками действительно заканчивай, вон глаза какие красные"
    menu:
        " - Мне все это просто снится... просто снится..":
            call Snitsa from _call_Snitsa
            return
        " - Что за?! Что происходит?":
            call ShoZa from _call_ShoZa
            return

label NeSpal:

    show alex at AlexLeft
    show ulearnich a at DedRight

    n " - Эй, [Alex], Я вообще-то все еще здесь!"
    menu:
        " - Что за?! Что происходит?":
            call ShoZa from _call_ShoZa_1
            return
        " - Я же должен быть в офисе один...":
            call Odin from _call_Odin
            return 


label Snitsa:
    n " - Переставай нудить, парень, я практически так же реален, как и ты"
    a " - Но... но... кто со мной общается сейчас? Кто ты... нет, что ты такое?!"
    return

label ShoZa:
    hide alex
    show alex a at AlexLeft
    a " - Наверное, просто глупый розыгрыш"
    n " - Да кому ты нужен, разыгрывать тебя ага, сидишь тут, штаны протираешь!"
    hide alex
    show alex at AlexLeft
    a " - Но... но... кто со мной общается сейчас? Кто ты... нет, что ты такое?!"
    return

label Odin:
    a " - Но... но... кто со мной общается сейчас? Кто ты... нет, что ты такое?!"
    return

label Zassal:
    hide ulearnich
    show alex a at AlexLeft
    show ulearnich a at DedRight

    a " - Блин, как-то стремно... Наверное, все же откажусь.."

    u " - Вот ты душнила! Давай, вошли и вышли! Приключение на 20 минут!"

    call NeZassal from _call_NeZassal_1
    return

label NeZassal:
    hide ulearnich
    hide alex
    show alex at AlexLeft
    show ulearnich at DedRight

    a " - Ну и ладно, терять мне уже нечего, выберу синюю"
    return

label Podumat:
    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich a at DedRight

    u " - Давай не тормози, иначе надоест мне с тобой возиться и оставлю тебя здесь одного"

    hide ulearnich
    show ulearnich at DedRight

    a " - Переубедил, пожалуй"
    a " - Но есть для начала что-нибудь совсем простое?"
    return

label Zatichka:
    return

label Lekciya:
    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich a at DedRight

    u " - Ах да. Я же забыл что вас учат только как писать кривой код"

    hide ulearnich
    show ulearnich at DedRight

    u " - Короче, щегол, краткий Ликбез. Ада Лавлейс - первый в истории программист. она написала свой алгоритм еще в 1843 году"

    hide alex
    show alex h at AlexLeft

    a " - Хаха, ну-ну, что-то ты мне впариваешь какую-то дичь, Компы то, только в 20 веке изобрели"

    hide ulearnich
    show ulearnich a at DedRight

    u " (вздох)"

    hide ulearnich
    show ulearnich at DedRight
    hide alex
    show alex at AlexLeft

    u " - на самом деле нет. Уже тогда был такой умный чел, звали его Бэббидж, который изобрел первый компьютер аж в 1822 году."
    u " - Конечно, компом назвать сейчас рука не поднимется, но тогда Ада написала для ЭТОГО компьютера свою программу."
    u " - А ты и на своем мощном ноуте ничего сделать не можешь ха-ха"

    hide alex
    show alex a at AlexLeft

    a " - Эй, обидно вообще то"

    hide alex
    show alex at AlexLeft

    a ' - Ну ладно, заинтересовал, так чего там с сайтом?'
    return

label Chistit:
    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich a at DedRight

    u " - А ну-ка, отставить такие мысли! Вперед и только вперед"
    return
  
label DaVrodeNorm:
    hide alex
    hide ulearnich
    show alex at AlexLeft
    show ulearnich a at DedRight

    u " - Надо же, норм ему, а сам недавно на аналогичную прогу орал, весь монитор забрызгал. Давай не отмазывайся, надевай перчатки, бери лопату и... "
    
    hide ulearnich
    show ulearnich at DedRight
    
    u " - Аа о чем это я, короче голыми руками давай исправляй, чтобы всё действительно норм работало"
    u " - Вот тут тебе в помощь оптимизированные куски кода, найди, куда их вставить и будет тебе счастье!"
    u " - Но помни: «Улучшение хорошо работающего продукта приводит к его ухудшению», так что не перестарайся"
    return



label MiniGame1:
    scene sitex

    play music minigame_music

    show alex at AlexLeft

    a "Это вообще реально починить?"

    show ulearnich h at DedRight

    u "Хочешь попробовать создать проект сайта снуля? Вот это настрой! Я тебя понял, РЕДАКТИРОВАНИЕ САЙТА!"

    scene white
    show alex a at AlexLeft

    a "Я имел ввиду на первый раз найти не такой безнадёжный проект..."

    show ulearnich at DedRight

    u "Что-то я поторопился. И вообще, кто минуту назад твердил, что готов?"
    u "Так что давай, не ной и почини это"

    call Cvet from _call_Cvet

    stop music fadeout 1.0

    return

label Cvet:
    scene white
    u "Для начала выбери подходящую палитру цветов цвет из предложенных"

    menu:
        "{image=Fones/Cvet/X.png}":
            call CvetR from _call_CvetR
        "{image=Fones/Cvet/N.png}":
            scene sitef
            u "У тебя хороший вкус!"
            call Shrift from _call_Shrift
        "{image=Fones/Cvet/Y.png}":
            call CvetR from _call_CvetR_1
        "{image=Fones/Cvet/I.png}":
            call CvetR from _call_CvetR_2

    return

label CvetR:
    u "Подумай ещё!"
    call Cvet from _call_Cvet_1
    return

label Shrift:
    u "Теперь тебе предстоит выбрать шрифт. Помни, что пользователь не должен всматриваться в текст"

    menu:
        "{image=Fones/Serif/N.png}":
            scene sites
            u "Да, этот подходит"
            u "Ну и куда же сайт без логотипа"
            call Logo from _call_Logo
        "{image=Fones/Serif/X.png}":
            call ShriftR from _call_ShriftR
        "{image=Fones/Serif/Y.png}":
            call ShriftR from _call_ShriftR_1
        "{image=Fones/Serif/I.png}":
            call ShriftR from _call_ShriftR_2

    return

label ShriftR:
    u "Увы, но ты ошибся"
    call Shrift from _call_Shrift_1
    return

label Logo:
    u "Помни, лого должно не только быть красивым и в хорошем качестве, но и подходить по стилю и цветам"

    menu:
        "{image=Fones/Logo/X.png}":
            call LogoR from _call_LogoR
        "{image=Fones/Logo/N.png}":
            scene sitel
            u "Действительно!"
            call FinishGame from _call_FinishGame
        "{image=Fones/Logo/Y.png}":
            call LogoR from _call_LogoR_1
        "{image=Fones/Logo/I.png}":
            call LogoR from _call_LogoR_2

    return

label LogoR:
    u "Ты уверен? Может ещё разок попробуешь?"
    call Logo from _call_Logo_1
    return


label MiniGame2:
    scene code

    play music minigame_music

    u "Думаю, ты уже догадался, что с кодом что-то не так"
    u "Тебе предстоить определить что именно"
    u "Специально для тебя я выделю проблемный участок, а ты выберешь верный из предложенных вариантов"
    u "Начнём!"

    call NameParams from _call_NameParams

    stop music fadeout 1.0

    return

label NameParams:
    scene code1
    u "Что не так в этом месте?"

    menu:
        " - Любой файл ОБЯЗАТЕЛЬНО нужно открывать так: \"with open(...) as ... \"":
            call NameParamsR from _call_NameParamsR
        " - Нужно использовать только двойные кавычки":
            call NameParamsR from _call_NameParamsR_1
        " - Нужно использовать только одинарные кавычки":
            call NameParamsR from _call_NameParamsR_2
        " - Непонятные названия вводимых переменных":
            u "Так и есть!"
            scene code2
            u "Идём дальше"
            call Cycle from _call_Cycle
    return

label NameParamsR:
    u "Не думаю, что проблема в этом"
    call NameParams from _call_NameParams_1
    return

label Cycle:
    menu:
        " - Лишний код. Нужно использовать цикл с заданным количеством повторов":
            scene code3
            u "Теперь взгляни на весь код целиком и выбери, чего же ещё такого важного мы не сделали"
            call CloseFile from _call_CloseFile
        " - Может быть здесь дело в кавычках?":
            call CycleR from _call_CycleR
        " - Вдруг одно условие сработает 2 раза? Никогда нельзя использовать \"elif\"":
            call CycleR from _call_CycleR_1
        " - Стоит делать отступы в одну строку после каждого условия":
            call CycleR from _call_CycleR_2
    return 

label CycleR:
    u "Я бы на твоём месте ещё раз подумал"
    u "Как-никак, за упавший вертолёт ответственность будет на тебе!"
    call Cycle from _call_Cycle_1
    return

label CloseFile:
    u "Смотри очень внимательно"
    menu:
        " - Не вижу никаких проблем":
            call CloseFileR from _call_CloseFileR
        " - Любой открытый файл должен закрываться":
            scene code4
            u "Действительно, тут даже я недоглядел"
            call FinishGame from _call_FinishGame_1
        " - В \"range\" цикла обязательно должен быть указан шаг цикла":
            call CloseFileR from _call_CloseFileR_1
        " - Последний \"else\" не нужен":
            call CloseFileR from _call_CloseFileR_2
    return

label CloseFileR:
    u "Хоть немного головой подумай, прежде чем тыкать"
    call CloseFile from _call_CloseFile_1
    return



label MiniGame3:
    return




label FinishGame:
    return