import random
import matplotlib.pyplot as plt

def simulate_dice_throws(n_simulations):
    sums = [0] * 11  # Масив для зберігання кількості випадків кожної суми від 2 до 12

    for _ in range(n_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums[dice_sum - 2] += 1  # Збільшуємо лічильник для відповідної суми

    probabilities = [(x / n_simulations) * 100 for x in sums]  # Обчислюємо ймовірності у відсотках
    return probabilities

def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    plt.bar(sums, probabilities)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум чисел при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

# Запускаємо симуляцію
n_simulations = 100000  # Кількість симуляцій (кідків кубиків)
probabilities = simulate_dice_throws(n_simulations)

# Відображаємо результати
plot_probabilities(probabilities)

# Порівняння з теоретичними значеннями
theoretical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

for i, (sim_prob, theor_prob) in enumerate(zip(probabilities, theoretical_probabilities)):
    print(f"Сума {i+2}: Симуляція = {sim_prob:.2f}%, Теорія = {theor_prob:.2f}%")
