items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_cost = 0
    chosen = []

    for name, info in sorted_items:
        if total_cost +info["cost"] <= budget:
            chosen.append(name)
            total_cost += info["cost"]
    return chosen 

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    res = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            res.append(names[i - 1])
            b -= items[names[i - 1]]["cost"]

    return res[::-1]

if __name__ == "__main__":
    budget = 100

    greedy_choice = greedy_algorithm(items, budget)
    dp_choice = dynamic_programming(items, budget)

    print(f"Greedy choice with budget {budget}: {greedy_choice}")
    print(f"DP choice with budget {budget}: {dp_choice}")