client_queue = []
client = ""

while True:
    client = input("Entre a name: ")
    if client.lower() == "paid":
        while client_queue:
            print(client_queue.pop())
        continue
    elif client.lower() == "end":
        print(len(client_queue))
        break

    client_queue.append(client)