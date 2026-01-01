def update_inventory(inventory, shipment):
    for item in shipment:
        if item[1] in [i[1] for i in inventory]:
            inventory[[i[1] for i in inventory].index(item[1])][0] += item[0]
        else:
            inventory.append(item)
    return inventory

if __name__ == "__main__":
    print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]))
    print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]))
    print(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]))
    print(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))