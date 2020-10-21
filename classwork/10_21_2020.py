# global variables
def _1():
    def main():
        get_name()
        print("Hello", name)
        
    def get_name():
        global name # <-python allows global assignment from local
        name = input("Enter your name: ")
        print(name)
        
    main()

# global variable quirks
def _2():
    number = -1
    def main():
        # below sets the LOCAL value of number
        # the global number is still -1 after this
        number = int(input("Enter the number: ")) 
        # you must set number as global number for the global to change
        show_number()
        
    def show_number():
        # below can only see the global variable number
        print("The number you entered is", number)
        
    main()