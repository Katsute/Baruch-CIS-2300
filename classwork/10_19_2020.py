# function
def _1():
    def main():
        print("I have a message for you.")
        message()
        print("Goodbye")
        
    def message():
        print("I'm Arthur")
        print("King of Britons")
        
    main()

# first/last
def _2():

    def main():
        print("Hello, my name is:")
        message()
        print("Nice to meet you.")
        
    def message():
        print("F")
        print("L")
        
    main()
    
# rep
def _3():

    def main():
        print("Hello, my name is:")
        for _ in range(0, 5):
            message()
        print("Nice to meet you.")
        
    def message():
        print("F")
        print("L")
        
    main()