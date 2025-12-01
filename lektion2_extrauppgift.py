data = {
"användare": [
("alice", {"ålder": 25, "roller": ("analyst", "vpn"), "aktiv": True}),
("bob", {"ålder": 22, "roller": ("webadmin",), "aktiv": False}),
("charlie", {"ålder": 23, "roller": ("analyst", "sql"), "aktiv": True}),
("diana", {"ålder": 24, "roller": ("vpn",), "aktiv": False}),
("eve", {"ålder": 21, "roller": ("analyst", "vpn", "sql"), "aktiv": True}),
],
"system": {
"analyst": {"användare": {"alice", "charlie", "eve"}},
"vpn": {"användare": {"alice", "diana", "eve"}},
"sql": {"användare": {"bob", "charlie", "eve"}},
}
}


lista_true = []
lista_false = []

for i in data["användare"]:
    user_name = i[0]
    user_data = i[1]
    if user_data["aktiv"] == True:
        lista_true.append(i)
    else:
        lista_false.append(i)


lista_roller = []
for i in lista_true:
    user_name = i[0]
    user_data = i[1]
    roller = user_data["roller"]
    for j in roller: 

        lista_roller.append(j)
        set(lista_roller)
    print(roller[0:])
print(lista_roller)



#print(lista_true)
#print(lista_false)