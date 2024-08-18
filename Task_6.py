items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# 1. Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_calories += info["calories"]
            total_cost += info["cost"]

    return selected_items, total_calories, total_cost

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм обрав: {selected_items}, калорії: {total_calories}, вартість: {total_cost}")


# 2. Динамічне програмування
def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [None] * (budget + 1)

    for item, info in items.items():
        for current_budget in range(budget, info["cost"] - 1, -1):
            if dp[current_budget - info["cost"]] + info["calories"] > dp[current_budget]:
                dp[current_budget] = dp[current_budget - info["cost"]] + info["calories"]
                selected_items[current_budget] = item

    total_calories = dp[budget]
    total_cost = 0
    result_items = []

    while budget > 0 and selected_items[budget]:
        result_items.append(selected_items[budget])
        total_cost += items[selected_items[budget]]["cost"]
        budget -= items[selected_items[budget]]["cost"]

    return result_items, total_calories, total_cost

selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print(f"Динамічне програмування обрало: {selected_items}, калорії: {total_calories}, вартість: {total_cost}")
