# coding=utf-8

# Erros e Exceções

# Try, Except, Finally
try:
    7 + 'b'
except TypeError:
    print("Operation not permitted")
    
# def askint():
#     try:
#         num = int(input("Enter a number: "))
#     except:
#         print("You didn't enter a number")
#     finally:
#         print("Thank you")
#     print(num)
        

# askint()

# Usando um loop

def askint():
    while True:
        try:
            num = int(input("Enter a number: "))
        except:
            print("You didn't enter a number: ")
        else:
            print("Thank you for entering a number")
            print(num)
            break
        finally:
            print("END")


askint()