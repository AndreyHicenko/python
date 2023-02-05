from flask import request, Flask, url_for
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1><center>Форма подачи заявки</center></h1>
                            <h3><center>на посещение объединений дополнительного образования</center></h3>
                            <h2><center>Точка роста</center></h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="patronymic" class="form-control" id="patronymic" placeholder="Введите Отчество" name="patronymic">
                                    <input type="date" class="form-control" id="date" placeholder="Введите дату рождения" name="date">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="clas">
                                          <option>5</option>
                                          <option>6</option>
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                     
                                     <div class="form-group">
                                        <label for="educprogrammSelect">Выберете образовательную программу</label>
                                        <select class="form-control" id="educprogrammSelect" name="educationalprogram">
                                          <option>Пограмма по биологии 6-9 классы</option>
                                          <option>Программа по химии 8-9 классы</option>
                                          <option>Программа по химии 10-11 классы</option>
                                          <option>Программа учебного курса "Мир генетики" 10 класс</option>
                                          <option>Программа учебного курса "Индивидуальный проект" 10 класс</option>
                                          <option>Программа учебного курса "Биологический эксперимент" 11 класс</option>
                                          <option>Программа учебного курса "Естествознание" 5 класс</option>
                                          <option>Программа учебного курса "Естествознание" 6-7 классы</option>
                                          <option>Программа по биологии 5-9 классы (по обновлённым ФГОС)</option>
                                          <option>Программа по технологии 6-9 классы</option>
                                          <option>Программа учебного курса "Технология: основы растениеводства" 6 класс</option>
                                          <option>Программа по технологии 5 класс (по обновлённым ФГОС)</option>
                                          <option>Программа учебного курса "Основы робототехники" 5 класс</option>
                                          <option>Программа учебного курса "Практическая физика" 10-11 классы</option>
                                          <option>Программа по физике 10-11 классы</option>
                                          <option>Программа по физике 7-9 классы</option>
                                          <option>Программа учебного курса "Практическая информатика" 10-11 классы</option>
                                          <option>Программа по информатике (информатике и ИКТ) 7-9 классы</option>
                                          <option>Программа по информатике (информатике и ИКТ) 10-11 классы</option>
                                          <option>Программа внеурочной деятельности "Здоровый образ жизни" 9 класс</option>
                                          <option>Программа внеурочной деятельности "Белая ладья" 1-4 класс</option>
                                          <option>Программа внеурочной деятельности "Белая ладья" 5 класс</option>
                                          <option>Программа внеурочной деятельности "Чудеса физики" 7 класс</option>
                                          <option>Программа внеурочной деятельности "Физика вокруг нас" 9 класс</option>
                                          <option>Программа внеурочной деятельности "Мы с компьютером на ТЫ" 6А класс</option>
                                          <option>Программа внеурочной деятельности "Мы с компьютером на ТЫ" 6Б класс</option>
                                          <option>Программа внеурочной деятельности "Мир мультимедиа" 8А класс</option>
                                          <option>Программа  "Кукла в ладошке"</option>
                                          <option>Программа  "Аксюшина мастерская"</option>
                                        </select>
                                     </div>
                                     
                                     
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="Мужской" checked>
                                          <label class="form-check-label" for="Мужской">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="Женский">
                                          <label class="form-check-label" for="Женский">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Подать заявку</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        datebase(request.form['name'], request.form['surname'], request.form['patronymic'],
                 request.form['date'], request.form['clas'], request.form['educationalprogram'],
                 request.form['about'], request.form['sex'])
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['patronymic'])
        print(request.form['date'])
        print(request.form['clas'])
        print(request.form['about'])
        print(request.form['sex'])

        return "Заявка отправлена"


def datebase(name, surname, patronymic, date, clas, educationalprogram, aboyt, sex):
    sqlite_connection = sqlite3.connect('datebase.db')
    cursor = sqlite_connection.cursor()
    sqlite_insert_query = f"""INSERT INTO tochka_rosta
                             (Имя, Фамилия, Отчество, [Дата рождения], Класс, [Образовательная программа], [О себе], Пол)
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (name, surname, patronymic, date, clas, educationalprogram, aboyt, sex)
    count = cursor.execute(sqlite_insert_query, data_tuple)
    sqlite_connection.commit()
    cursor.close()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
