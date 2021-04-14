def encrytor(text):
    encrypted_text = ""
    for i in text:
        if i in "aA":
            encrypted_text = encrypted_text + str(1)
        elif i in "bB":
            encrypted_text = encrypted_text + str(2)
        elif i in "cC":
            encrypted_text = encrypted_text + str(3)
        elif i in "dD":
            encrypted_text = encrypted_text + str(4)
        elif i in "eE":
            encrypted_text = encrypted_text + str(5)
        elif i in "fF":
            encrypted_text = encrypted_text + str(6)
        elif i in "gG":
            encrypted_text = encrypted_text + str(7)
        elif i in "hH":
            encrypted_text = encrypted_text + str(8)
        elif i in "iI":
            encrypted_text = encrypted_text + str(9)
        elif i in "jJ":
            encrypted_text = encrypted_text + str(10)
        elif i in "kK":
            encrypted_text = encrypted_text + str(11)
        elif i in "lL":
            encrypted_text = encrypted_text + str(12)
        elif i in "mM":
            encrypted_text = encrypted_text + str(13)
        elif i in "nN":
            encrypted_text = encrypted_text + str(14)
        elif i in "oO":
            encrypted_text = encrypted_text + str(15)
        elif i in "pP":
            encrypted_text = encrypted_text + str(16)
        elif i in "qQ":
            encrypted_text = encrypted_text + str(17)
        elif i in "rR":
            encrypted_text = encrypted_text + str(18)
        elif i in "sS":
            encrypted_text = encrypted_text + str(19)
        elif i in "tT":
            encrypted_text = encrypted_text + str(20)
        elif i in "uU":
            encrypted_text = encrypted_text + str(21)
        elif i in "vV":
            encrypted_text = encrypted_text + str(22)
        elif i in "wW":
            encrypted_text = encrypted_text + str(23)
        elif i in "xX":
            encrypted_text = encrypted_text + str(24)
        elif i in "yY":
            encrypted_text = encrypted_text + str(25)
        elif i in "zZ":
            encrypted_text = encrypted_text + str(26)
        elif i in " ":
            encrypted_text = encrypted_text + str(0)

    return encrypted_text


text = str(input("Enter text : "))
print(encrytor(text))
