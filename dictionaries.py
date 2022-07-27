n = int(input())
contacts = {}

for i in range(0, n):
    name, phone = input().split(' ')
    contacts[name] = phone

for i in range(0, n):
    read_name = input()
    if 1 <= n and n <= 100000:
        if 1 <= len(contacts) and len(contacts) <= 100000:
            if read_name in contacts:
                print(read_name+'='+contacts[read_name])
            else:
                print('Not found')