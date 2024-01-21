items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

sorted_items = sorted(items.items(), key=lambda x: x[1])
current_weight = 0.0
backpack = {}

for item, weight in sorted_items:
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight

print(backpack)
