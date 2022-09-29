def show_messages(list):
    print("The messages in the first list:")
    for msg in list:
        print(msg)
    print()


def send_messages(og_list, new_list):
    print("Printing each text message and then moving it to the new list:")
    while og_list:
        current_msg = og_list.pop()
        print(current_msg)
        new_list.append(current_msg)
    print()


messages = ["Hello", "Deez nutz", "What's the hw?", "Ok"]
sent_messages = []

show_messages(messages)
send_messages(messages[:], sent_messages)

print("Printing both lists after moving messages:")
print("First list:", messages)
print("Second list:", sent_messages)