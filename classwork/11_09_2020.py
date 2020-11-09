# recursion
def main():
    message(5)
    message_loop(5)
    
def message(times):
    if times > 0:
        print("This is a recursive function.")
        message(times - 1)
        
def message_loop(times):
    for _ in range(times):
        print("This is a for loop.")

main()