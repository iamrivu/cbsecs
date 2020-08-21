# a list
keys = ["john", "Milar", "Ketty"]
values = ["Python", "PHP", "Java"]
# a dictionary with lists
data = dict(zip(keys,values))
print(data)
# add new data
data["Jerry"] = "CS"
print(data)
# delete value using key
del data["Jerry"]
print(data)

# dictionary,list inside a dictionary
prog = {"JS":"Atom", "CS":"VS", "Python":["Pycharm","VSCode","Sublime"],"Java":{"J2SE":"Netbeans","J2EE":"Eclipse"}}
print(prog)
print(prog["JS"])
print(prog["Python"])
print(prog["Python"][0])
print(prog["Java"])
print(prog["Java"]["J2EE"])