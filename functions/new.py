def getsum(*numberz):
    total=0
    for num in numberz:
        total+=num
    return total
def create_sentence(**words):
    print(words)
    sentence=" "
    for word in words.values():
        sentence+=word
        sentence+=" "
    return sentence
def sum_and_greet(*args, **kwargs):
    total=0
    for x in args:
        total+=x
    f=kwargs["first_name"]
    l=kwargs["last_name"]
    greeting=f"Hello {f} {l} total of your number is {total}"
    return greeting
