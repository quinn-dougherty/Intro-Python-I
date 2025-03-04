# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

if __name__=='__main__':
    # When you use a variable in a function, it's local in scope to the function.
    x = 12

    def changeX():
        global x
        x = 99

    changeX()

    # This prints 12. What do we have to modify in changeX() to get it to print 99?
    print(x) # `global x` inside function


    # This nested function has a similar problem.

    def outer():
        y = 120

        def inner():
            nonlocal y
            y = 999

        inner()

        # This prints 120. What do we have to change in inner() to get it to print
        # 999? Google "python nested function scope".
        print(y) # put `nonlocal y` inside `inner`

    outer()
