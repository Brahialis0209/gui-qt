
# Reference in English
This application is for solving the linear programming problem by the simplex method.
## Requirements
- Python 3.6-3.8
- packages indicated in `requirements.txt`
## Install, launch, uninstall
- create a copy of the repository: `git clone https://gitlab.com/Brahialis0209/gui-qt.git`
- open the `gui-qt` folder as a PyCharm project and run `src/main.py`
or, being in the `gui-qt/src` folder, execute the command:`python main.py`
## Work with the application
- First you need to select the number of lines (number of restrictions), the number of variables and press `Ввести`.
- Next, it is proposed to introduce coefficients for the set of constraints, for the objective function and restrictions on the unknown, <br>
 the `extreme` column is responsible for maximizing or minimizing your objective function.
- Further, if you entered the data correctly, click `Посчитать`. <br> If the input was incorrect (letter instead of number) -
  You will receive an error message about exactly where the wrong input was.
- With the correct data, you will receive a response.
- Also, if the dimension of the problem = 2, (two variables), then the application will suggest constructing a graph of iterations <br>
  when finding the optimal solution.
- Use the magnifier in the panel to enlarge the image.
### Example
#### The next task was taken as an example.
![gui](images/example1_widgets.png)<br>
#### Here you can see the initial approximation as well as 2 support solutions located on the polyhedron of constraints.
![gui](images/example1_graph.png)


# Reference in Russian
Это приложение для решения задачи линейного программирования симплекс-методом.
## Требования
- Python 3.6-3.8
- пакеты, указанные в `requirements.txt`
## Установка, запуск, удаление
- создайте копию репозитория: `git clone https://gitlab.com/Brahialis0209/gui-qt.git`
- откройте папку `gui-qt` как проект PyCharm и запустите `src/main.py`
либо, находясь в папке `gui-qt/src`, исполните команду: `python main.py`
## Работа с приложением
- Сперва нужно выбрать число строк(число ограничений), число переменных и нажать `Ввести`.
- Далее предлагается ввести коэффициенты для множества ограничений, для функции цели и ограничения на неизвестные,<br>
 колонка `extreme` отвечает за максимизацию или минимизацию вашей целевой функции.
- Далее, если вы ввели данные корректно, нажмите `Посчитать`.<br> В случае, если ввод был некорректным(буква вместо числа) -
  вы получите сообщение об ошибке и о том где именно был неправильный ввод.
- При корректных данных вы получите ответ.
- Также, если размерность задачи = 2, (две переменные) то приложение предложит построить график итераций<br>
  при нахождении оптимального решения.
- Для увеличения изображения используйте лупу в панели.
### Пример
#### Следующая задача была взята как пример.
![gui](images/example1_widgets.png)<br>
#### Тут можно увидеть начальное приближение а также 2 опорных решения, расположенных на многограннике ограничений.
![gui](images/example1_graph.png)
