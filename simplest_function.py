def greet():
    print("hello dear, hope you´re doing fine")


for i in range(10):
    print(f"{i+1} ", end="")
    greet()

x = greet()
print(x)
y = print("hello world")
print(y)
