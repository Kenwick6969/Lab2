def display_main_menu():
    print("display_main_menu")

def calculate_temperature(Temperatures):
    """ Calculate The Average, Minimum And Maximum Temperature From A List Of Temperatures. """
    print("Calculating Temperature...") #Message To Indicate Code Is Working

    list.sort(Temperatures)
    Average = float(sum(Temperatures) / len(Temperatures))
    Maximum = max(Temperatures)
    Minimum = min(Temperatures)
    Median = (Temperatures)[len(Temperatures) // 2]

    print ("The Average Temperature Is: " + str(Average)) #Output The Average
    print ("The Maximum Temperature Is: " + str(Maximum)) #Output The Maximum
    print ("The Minimum Temperature Is: " + str(Minimum)) #Output The Minimum
    print ("The Median Temperature Is: " + str(Median)) #Output The Median
    print ("The Sorted List Of Temperatures Is: " + str(Temperatures)) #Output The Sorted List


user_input = []

def main():
    """ Main Menu For Temperature Calculator """
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")   
    x = True

    print ("Welcome To The Temperature Calculator!") #Welcome Message
    print ("Please Input The Temperature Values You Wish To Calculate: ")

    while x == True: #Loop To Allow Multiple Inputs
        Values = input("Temperature Value: ") #User Input For Temperature Value

        if Values.isdigit() == False: #Check If The Input Is A Number
            print ("Invalid Input, Please Try Again!") #Invalid Input

        else:
            user_input.append(float(Values)) #Insert The Temperature Values Into The List
            Continue = str(input("Do You Wish To Continue? (Y/N): ")) #Asking User If They Wish To Continue
            Continue = Continue.upper()
            
            if Continue == "Y" or Continue == "YES":
                x == True #Continue Loop

            elif Continue == "N" or Continue == "NO": 
                user_input.clear() #Clear The List To Avoid Issues With Multiple Runs
                break #Exit Loop
            
            else:
                print ("Invalid Input, Please Try Again!") #Invalid Input
                user_input.clear() #Clear The List To Avoid Issues With Multiple Runs
                break
    
    print ("The Temperature Values You Inputted Are: " + str(user_input)) #Output The Temperature Values

    calculate_temperature(user_input) #Calculation

if __name__ == "__main__":
    main()