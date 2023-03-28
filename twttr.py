def main():
    txt = get_input("Input: ")
    print("Output: ",end="")
    convert(txt)

def get_input(prompt):
    return input(prompt)

def convert(t):
    for letter in t:
        if not letter.lower() in ["a","e","i","o","u"]:
            print(letter, end="")
    print()

main()