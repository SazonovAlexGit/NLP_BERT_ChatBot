# NLP BERT Futurama Fry ChatBot
## Задание:
Необходимо разработать чат-бота, используя подход retrieval-based. Бот должен вести диалог как определенный персонаж сериала, имитируя стиль и манеру конкретного персонажа сериала. Важно учесть особенности речи и темы, которые поднимает персонаж, его типичные реакции.

## Данные
В качестве основы для чат-бота была взята транскрипция диалогов к мультсериалу "Футурама", которые есть на Kaggle и можно загрузить по [cсылке](https://www.kaggle.com/datasets/josephvm/futurama-seasons-16-transcripts?select=only_spoken_text.csv).

Основной персонаж бота - Филипп Фрай мл. (Philipp J. Fry)
![Fry](https://w.forfun.com/fetch/b0/b05c44a3811bda8d30cb936f6673e777.jpeg)

## Данные
В файле данные распределын по репликам персонажей

Обработка данных подразумевает следующие шаги:
- отбор реплик персонажа в качестве ответов / answers. Фильтр по полю "Charakter speaking" == 'Fry'
- отбор реплик всех остальных персонажей к Фраю / questions. Фильтр по полю "Charakter speaking" != 'Fry'
- загрузка реплик в соответствующие датасеты средствами Pandas

Функции для обработки данных находятся в файле model.py
Сами данные находятся /data/fry.csv

## Обучение
Для обучения был выбран алгоритм bi-encoder (SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')) / cross-encoder (CrossEncoder('ms-marco-MiniLM-L-6-v2'))
База данных реплик включает векторизованные при помощи модели обученного_энкодера скрипты, включающие ответ персонажа, а так же закондированные cross-encoder вопросы к персонажу.

Отбор реплик из базы данных проводился следующим образом:
- отбор наилучшего результата из созданной векторной базы данных. В результате отбирается ответ с максимальным скорингом похожести на пользовательский вопрос.
   
## Реализация web-сервиса
С помощью библиотеки Flask был реализован простой веб интерфейс с полем для ввода вопроса и кнопкой «Send».
Веб-сервер доступен по адресу http://localhost:5000

## Использование чат-бота:
+ pip install -r requirements.txt
+ run main.py
+ Open link [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web-browser
+ Chat with Fry
  > Remember: Fry not smart boy 
