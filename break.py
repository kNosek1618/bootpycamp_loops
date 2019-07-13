
while True:
    command = input("Type 'exit' to exit: ")
    if command == "exit":
        break

for x in range(1,10):
    print(x)
    if x == 3:
        print("closing program . .")
        break