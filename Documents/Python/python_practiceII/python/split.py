def mysplit(strng):
    elem = ""
    list_chars = []
    for ch in strng:
        if ch.isalnum():
            elem += ch
        else:
            if elem != "":
                list_chars.append(elem)
            elem = ""
    if elem != "":
        list_chars.append(elem)
    return list_chars


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))