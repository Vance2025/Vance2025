def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "undo":
            undone = history.pop()   # pop()是一个方法，用于从列表中删除最后一个元素并返回该元素
            print(f"Undone: {undone}")
        elif action == "restart":
            history.clear()    # clear()是一个方法，用于清空列表中的所有元素
            print("Game restarted. History cleared.")
        else:
            history.append(action)
            print(history)


main()