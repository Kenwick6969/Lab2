def calculate_bmi(Weight, Height):
    """ Calculate Body Mass Index (BMI) Given Weight In Kilograms And Height In Meters. """
    print ("Height(Kilograms) = " + str(Height)) #Output The Initial Height Value
    print ("Weight(Meters) = " + str(Weight)) #Output The Initial Weight Value

    BodyMassIndex = Weight / (Height*Height) #Calculation Of BMI

    print ("Body Mass Index (BMI) = " + str(BodyMassIndex)) #Output The Calculated BMI Value

    #BMI Categories
    if BodyMassIndex < 18.5:
        print ("BMI Weight Classification: Underweight") #Weight Classification Underweight

    elif 18.5 <= BodyMassIndex < 25:
        print ("BMI Weight Classification: Normal Weight") #Weight Classification Normal Weight

    elif 25 <= BodyMassIndex < 50:
        print ("BMI Weight Classification: Overweight") #Weight Classification Overweight

    else:
        print ("BMI Weight Classification: OH HELL NO! YOU ARE BEYOND OVERWEIGHT! PLEASE GET SOME HELP!") #Weight Classification Whale

calculate_bmi(79.9,1.805)