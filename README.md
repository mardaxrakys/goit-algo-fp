# Task_1
## Опис функцій:
- reverse — ця функція змінює посилання між вузлами, реверсуючи однозв'язний список.
- insertion_sort — ця функція реалізує сортування вставками для однозв'язного списку.
- sorted_merge — ця функція об'єднує два відсортовані однозв'язні списки в один відсортований список.

### Використання:
- Реверсування: Створюється список llist1, який потім реверсується і виводиться на екран.
- Сортування: Створюється інший список llist2, який сортується за допомогою сортування вставками і виводиться на екран.
- Об'єднання: Обидва відсортовані списки об'єднуються у новий список merged_list, який потім виводиться на екран.

# Task_2 
## Опис програми:
### 1. Функція draw_pythagoras_tree(t, length, level):

- t — об'єкт Turtle.
- length — довжина сторони квадрата.
- level — рівень рекурсії. З кожним рівнем квадрати стають меншими, і програма викликає функцію рекурсивно для малювання нових "гілок".
### 2. Рекурсія:

- На кожному рівні рекурсії програма малює квадрат, а потім викликає себе двічі для лівої та правої гілок дерева, зменшуючи розмір квадрата.
- Рекурсія завершується, коли level стає 0.
### 3. Функція main():

- Створює вікно Turtle та об'єкт Turtle для малювання.
- Запитує у користувача рівень рекурсії.
- Встановлює початкову позицію Turtle та викликає функцію для малювання дерева Піфагора.
## Як використовувати:
- Запустіть програму.
- Введіть бажаний рівень рекурсії (наприклад, від 1 до 10). Зазвичай, значення рівня понад 10 може викликати тривале виконання та перевантаження графіки.
- Спостерігайте, як Turtle малює фрактал "Дерево Піфагора".

# Task_3
## Опис програми:
### Граф:

- Граф представлений у вигляді словника, де ключами є вершини, а значеннями — словники з сусідніми вершинами та відповідними вагами ребер.
### 1. Функція dijkstra(graph, start):

- graph — це вхідний граф, представлений як словник.
- start — початкова вершина, від якої потрібно знайти найкоротші шляхи.
- distances — словник, де зберігаються мінімальні відстані від початкової вершини до всіх інших. Ініціалізується як нескінченність для всіх вершин, крім початкової (яка має 0).
- priority_queue — черга пріоритетів, що використовує бінарну купу (heapq). Вона містить пари (відстань, вершина), де відстань визначає пріоритет (менша відстань має вищий пріоритет).
- Алгоритм:

### 2. Алгоритм продовжує працювати поки черга пріоритетів не порожня.
- На кожному кроці алгоритм витягує вершину з мінімальною відстанню з черги.
- Перевіряє всі суміжні вершини та оновлює їх відстані, якщо знайдено коротший шлях.
- Якщо оновлено відстань, вершина додається назад у чергу з новою відстанню.
### 3. Виведення результатів:

- Для кожної вершини графа виводиться найкоротша відстань від початкової вершини.
### Як використовувати:
- Задайте граф у вигляді словника, де ключами є вершини, а значеннями — інші словники з сусідніми вершинами та вагами ребер.
- Викличте функцію dijkstra(graph, start), передавши граф і початкову вершину.
- Отримані результати міститимуть найкоротші шляхи від початкової вершини до всіх інших.

# Task_4
## Пояснення:
### 1. Клас Node:

- Представляє вузол дерева. Кожен вузол має посилання на лівого і правого нащадка, значення, колір та унікальний ідентифікатор.
### 2. Функція add_edges:

- Рекурсивно додає ребра між вузлами у графічному представленні дерева.
### 3. Функція draw_tree:

- Відповідає за візуалізацію дерева з використанням бібліотек networkx і matplotlib.
### 4. Функція build_heap_tree:

- Створює дерево на основі масиву, який було перетворено на бінарну купу.
### Приклад використання:

- Масив array перетворюється на бінарну купу за допомогою функції heapq.heapify.
- Функція build_heap_tree будує дерево з цього масиву, після чого функція draw_tree відображає дерево.

# Task_5
## Пояснення:
### 1. Клас Node:

- Вузол дерева має значення (val), посилання на лівого і правого нащадка (left, right), колір (color) та унікальний ідентифікатор (id).
### 2. Функція add_edges:

- Рекурсивно додає вузли та ребра між ними до графу для побудови візуалізації дерева.
### 3. Функція draw_tree:

- Візуалізує дерево з використанням кольорів, що змінюються в залежності від порядку обходу.
### 4. Функція bfs (Обхід в ширину):

- Використовує чергу (deque) для обходу дерева рівень за рівнем. Кожному вузлу присвоюється колір із поступовим переходом від темного до світлого (через список кольорів).
### 5. Функція dfs (Обхід в глибину):

- Використовує стек для обходу дерева гілка за гілкою. Кольори змінюються аналогічно BFS.
### Приклад використання:

- Створюється дерево, після чого відбувається візуалізація обходу цього дерева як в ширину (BFS), так і в глибину (DFS).

# Task_6
## Пояснення:
### 1. Жадібний алгоритм:

- Спочатку всі страви сортуються за співвідношенням калорій до вартості.
- Далі, починаючи з найбільшого співвідношення, страви додаються до вибору, доки не буде вичерпано бюджет.
### 2. Алгоритм динамічного програмування:

- Використовується підхід з побудовою динамічної таблиці (масиву dp), де dp[i] містить максимальну кількість калорій, яку можна отримати при наявності бюджету i.
- Програма ітеративно заповнює таблицю, розглядаючи кожну страву та її вартість, і визначає, чи потрібно додавати її до вибору.

# Task_7
## Пояснення:
### 1. simulate_dice_throws(n_simulations):
- Функція симулює кидання двох кубиків задану кількість разів (n_simulations) і підраховує частоту кожної можливої суми (від 2 до 12). Потім вона обчислює ймовірність кожної суми у відсотках.

### 2. plot_probabilities(probabilities):
- Функція будує стовпчасту діаграму ймовірностей для кожної суми.
### 3. n_simulations:
- Кількість симуляцій, яку ви можете змінити залежно від необхідної точності.

### 4. - Після симуляції ми порівнюємо отримані ймовірності з теоретичними значеннями, які наведені у вашій таблиці.

## Результат:
- Програма відображає ймовірності для кожної можливої суми після симуляції.
- У кінці коду є порівняння симуляційних результатів із теоретичними значеннями, щоб оцінити точність методу Монте-Карло.
