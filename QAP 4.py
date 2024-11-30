# Description: A program that calculates the insurance policy of the One Stop Insurance Company
# Author: Brady Keats
# Date(s): November 16th 2024 - November 29th 2024


# Define required libraries.
import FormatValues as FV

# Define program constants.
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_FOR_ADD_CARS = .25
EXTRA_LIABILITY_COVERAGE = 130.00
COST_GLASS_COVERAGE = 86.00
LOANER_CAR_COVERAGE = 58.00
HST_RATE = .15
PROCESSING_FEE_MONTHLY_PAYMENTS = 39.99
PROVINCE_LIST = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
PAYMENT_LIST = ["Full", "Monthly", "Down"]
YES_NO_LIST = ["Y", "N"]


# Define program functions.

#Customers info
while True:
    CustFirstName = input("Enter the customers first name: ").title()
    if CustFirstName == "":
        print()
        print("Data entry error - customers first name must be entered...")
        print()
    else:
        break

while True:
    CustLastName = input("Enter the customers last name: ").title()
    if CustLastName == "":
        print()
        print("Data entry error - customers last name must be entered...")
        print()
    else:
        break

while True:
    StAdd = input("Enter the street address: ")
    if StAdd == "":
        print()
        print("Data entry error - address must be entered...")
        print()
    else:
        break

while True:
    City = input("Enter the city name: ").title()
    if City == "":
        print()
        print("Data entry error - city must be entered...")
        print()
    else:
        break


# Validation using a list.

 
while True:
    Prov = input("Enter the province (XX): ").upper()
 
    if Prov == "":
        print("   Data Entry Error - Province cannot be blank.")
    elif len(Prov) != 2:
        print("   Data Entry Error - Provice is a 2 character code only.")
    elif Prov not in PROVINCE_LIST:
        print("   Data Entry Error - province is not valid.")
    else:
        break
while True:
    PostalCode = input("Enter the postal code(X#X#X#): ")
    if len(PostalCode) != 6:
            print()
            print("Data entry error - postal code must be 6 characters...")
            print()
    else:
        break
    
while True:
     PhoneNum = input("Enter the customers phone number(0000000000): ")

     if PhoneNum == "":
            print()
            print("     Data Entry Error Occured Customers Phone Number must be entered ")
            print()
     elif len(PhoneNum) != 10:
            #
            print()
            print("     Data Entry Error Occured Customers Phone Number must be 10 digits ")
            print()
     elif PhoneNum.isdigit() == False:
             #
            print()
            print("     Data Entry Error Occured Customers Phone Number must be 10 digits ")
            print()
     else:
            break

    

#Details of the cars

while True: 
        NumCarsInsured = input("Enter the number of cars being insured: ")
        NumCarsInsured = int(NumCarsInsured)
        break

while True:
        ExtraLiability = input("Would you like to have extra liability (Y or N): ").upper()
        if ExtraLiability == "":
            print()
            print("Data entry error - Must enter (Y or N)...")
            print()

        elif ExtraLiability not in YES_NO_LIST:
            print()
            print("Data entry error - Must enter (Y or N)...")
            print()
        
        else:
            break

        if ExtraLiability == "Y":
            ExtraLiabilityMsg = "Yes"
            ExtraLiabilityCost = EXTRA_LIABILITY_COVERAGE * NumCarsInsured
           
        else:
            ExtraLiabilityMsg = "No"
            ExtraLiabilityCost = 0.0

while True:
        GlassCover = input("Would you like glass coverage (Y or N): ").upper()
        if GlassCover == "":
            print()
            print("Data entry error - Must enter (Y or N)...")
            print()

        elif GlassCover not in YES_NO_LIST:
            print()
            print("Data entry error - Must enter (Y or N)...")
            print()

        elif GlassCover == "Y":
            GlassCoverMsg = "Yes"
            GlassCost = COST_GLASS_COVERAGE * NumCarsInsured
            break

        else:
            GlassCoverMsg = "No"
            GlassCost = 0.0
            break

while True:
        LoanerCar = input("Would you like a loaner car (Y or N): ").upper()
        if LoanerCar == "":
            print()
            print("Data entry error - Must enter (Y or N)...")
            print()

        elif LoanerCar not in YES_NO_LIST:
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()

        elif LoanerCar == "Y":
            LoanerCarMsg = "Yes"
            LoanCarCost = LOANER_CAR_COVERAGE * NumCarsInsured
            break

        else:
            LoanerCarMsg = "No"
            LoanCarCost = 0.0
            break

def CalculateTotalPremium(NumCarsInsured, ExtraLiabilityCost, GlassCost, LoanCarCost, DownPayAmt):
    AddCarPremium = 0
    BasePrem = BASIC_PREMIUM

    if NumCarsInsured > 1:
        AddCarPremium = BASIC_PREMIUM - (BASIC_PREMIUM * DISCOUNT_FOR_ADD_CARS)

    ExtraCost = ExtraLiabilityCost + GlassCost + LoanCarCost
    TotalInsurancePrem = (BasePrem + AddCarPremium + ExtraCost)
    NewTotalInsurancePremium = TotalInsurancePrem - DownPayAmt
    HST = NewTotalInsurancePremium * HST_RATE
    Total = NewTotalInsurancePremium + HST


# Main program starts here.
print()
while True:
    
    # Gather user inputs.

    #Choosing a Payment method

        while True:
            PaymentChoice = input("How would you like to pay (Full or Monthly): ").title()
            if PaymentChoice not in PAYMENT_LIST:
                print()
                print("   Data Entry Error - Payment option is not valid...")
                print()
            else:
                break


            if PaymentChoice == "Full":
             PaymentMsg = "Thanks for paying in full"
             DownPay = 0
             DownPayMsg = "No"
             DownPayChoice = "N"
    
            if PaymentChoice == "Monthly":
                PaymentMsg = "Payment will consist of 8 monthly payments"
    
        while True:
            DownPayMsg = "No"
            DownPay = 0
            DownPayChoice = input("Would you like to make a down payment ( Y or N ): ").upper()
            if DownPayChoice == "":
                print()
                print("Data entry error - Must enter ( Y or N )...")
                print()
            elif set(DownPayChoice).issubset(YES_NO_LIST) == False:
                print()
                print("Data entry error - Must enter ( Y or N )...")
                print()
            else:
                break

        if DownPayChoice == "Y":
            DownPayMsg = "Yes"
            while True:
                try:
                    DownPay = input('Enter the amount of $ you would like to down pay: ')
                    DownPay =float(DownPay)

                except:
                    print()
                    print("Data entry error - Downpayment must be a valid number...")
                    print()
                else:
                    break

        

    # Perform required calculations.

        TotalInsurancePrem, Tax, Total, ExtraCost, AddCarPremium, BasePrem, DownPay, NewTotalInsurancePrem = CalculateTotalPremium(NumCarsInsured, ExtraLiability, GlassCost, LoanCarCost, DownPay)

    
        if PaymentChoice == "Monthly":
            if DownPayChoice == "Y":
                Cost = (Total + PROCESSING_FEE_MONTHLY_PAYMENTS) / 8
            else:
                Cost = (Total + PROCESSING_FEE_MONTHLY_PAYMENTS) / 8
        else: 
            Cost = Total


        InvoiceDate = input("Enter the date: ")


        if PaymentChoice == "Monthly":
            NewTotal = Total + PROCESSING_FEE_MONTHLY_PAYMENTS


    # Display results

        print()
        print(f"      One Stop Insurance Company                                         ")
        print(f"-----------------------------------------------------------              ")
        print(f"Invoice date:                 {InvoiceDate:>10s}                         ")
        print(f"Policy number:                {POLICY_NUMBER:>2d}                        ")

        print()
        print(f"First name: {CustFirstName:>12s}    Last name: {CustLastName:>12s}       ")
        print(f"Street Adress:      {StAdd:>20s}    City:  {City:>20s}                   ")
        print(f"Province:      {Prov:>2s}           PostalCode:   {PostalCode:>7s}       ")
        print(f"Phone Number:             {PhoneNum:>14s}                                ")
        print(f"-------------------------------------------------------------            ")

        print()
        print(f"Number of cars insured:               {NumCarsInsured:>2d}               ")
        print(f"Price for first car:           {FV.FDollar2(BasePrem):>9s}               ")
        if NumCarsInsured >1:
            print(f"Price for extra cars:          {FV.FDollar2(AddCarPremium):>9s}      ")
        print(f"--------------------------------------------------------------           ")

        print()
        print(f"Extra liability coverage:            {ExtraLiabilityMsg:>3s}             ")
        print(f"Glass Coverage:                      {GlassCoverMsg:>3s}                 ")
        print(f"Loaner car:                          {LoanerCarMsg:>3s}                  ")

        print()
        if ExtraLiability == "Y":
            print(f"Extra liability coverage cost: {FV.FDollar2(ExtraLiability):>9s}     ")

        if GlassCover == "Y":
            print(f"Glass Coverage cost:           {FV.FDollar2(GlassCost):>9s}          ")

        if LoanerCar == "Y":
            print(f"Loaner car cost:               {FV.FDollar2(LoanCarCost):>9s}        ")
        
        print(f"  ------------------------------------------------------------           ")
        print(f"Total Extra fees:              {FV.FDollar2(ExtraCost):>9s}              ")
        print(f"--------------------------------------------------------------           ")

        print()
        if PaymentChoice == "Monthly":
            print(f"Processing fee:    {FV.FDollar2(PROCESSING_FEE_MONTHLY_PAYMENTS):>6s}")
            print(f"                              ----------")
            print(f"New Total Premium:             {FV.FDollar2(NewTotal):>9s}           ")
            print()
            print(f"Payment option:                  {PaymentChoice:>7s}                 ")
        if PaymentChoice == "Full":
            print()
            print(f"----- {PaymentMsg} -----")
        if PaymentChoice == "Monthly":
            print(f"Monthly Payment:               {FV.FDollar2(Cost):>9s}               ")
            print()

        if PaymentChoice == "Monthly":
            print(f"Down Payment:                        {DownPayMsg:>3s}                 ")
        if DownPayChoice == "Y":
            print(f"Balance Before Downpayment:    {FV.FDollar2(TotalInsurancePrem):>9s}  ")
            print(f"Down Payment amount:         - {FV.FDollar2(DownPay):>9s}             ")
            print(f"                              ----------                              ")
        print(f"Insurance Premium:             {FV.FDollar2(NewTotalInsurancePrem):>9s}   ")
        print(f"HST (15%):                     {FV.FDollar2(Tax):>9s}                     ")
        print(f"                              ----------")
        print(f"Total Premium:                 {FV.FDollar2(Total):>9s}                   ")
    



        Continue = input("Would you like to enter another insurance policy (Y/N): ").upper()
        if Continue == "N":
            print("Thank you for using the One Stop Insurance Company!")
            break
        else:
            continue
    