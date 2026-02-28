def count_change(change):
    total = 0
    for i in change:
        total += i
    totalFloated = total * 0.01
    totalStringed = f"${round(totalFloated, 2):.2f}"
    return totalStringed


print(count_change([25, 10, 5, 1]))
