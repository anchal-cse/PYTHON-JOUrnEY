# def function(): # local variable it tell the python what the function should do :-it define the function
#     a = 10
#     print(a)

# function()# to execute the function we have to call itby its name 
#            #without calling the function it will not execute the function only defining the function will not execute it



# a = 20 

# def function(): #glob variable
#     print(a)

# function()
# print(a)

a = 20

def function():
    global a
    a = a + 2

function()
print(a)
