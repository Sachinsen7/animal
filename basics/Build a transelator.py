def transelate(phrase):
    transelation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            transelation = transelation + "g"
        else:
            transelation = transelation + letter
    return transelation


print(transelate(input("Enter a phrase ")))



def transelate(phrase):
    transelation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transelation = transelation + "G"
            else:
                transelation = transelation + "g"
        else:
            transelation = transelation + letter
    return transelation

print(transelate(input("Enter a phrase ")))









