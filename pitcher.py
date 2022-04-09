# function of ERA

def era_formula(inning,earned_run):
    try:
        era = float((9/float(inning))*float(earned_run))
        print("\nthe pitcher pitched " + str(inning) + " innings")
        print("the pitcher lost " + str(earned_run) + " earned runs")
        print("the ERA of this pitcher is "+str(era))
    except ValueError:
        print(str(inning) + " or " + str(eraned_run) + " is not the number, PLEASE TYPE AGAIN  ")

# functions of K9

def k9_formula(inning,strike_out):
    try:
        k9 = float((9/inning)*strike_out)
        print("\nthe pitcher pitched " + str(inning) + " innings")
        print("the pitcher got " + str(strike_out) + " strike_out")
        print("the K9 of this pitcher is "+str(k9))
    except ValueError:
        print(str(inning) + " or " + str(strike_out) + " is not the number, PLEASE TYPE AGAIN  ")

def bb9_formula():
    inning = float(input("\nplease input the inning of pitcher\n"))
    base_on_balls = float(input("please input the number of base on balls of pitcher\n"))
    k9 = float((9/inning)*base_on_balls)
    print("\nthe pitcher pitched " + str(inning) + " innings")
    print("the pitcher got " + str(base_on_balls) + " base on balls")
    print("the BB9 of this pitcher is "+str(bb9))

def whip_formula():
    inning = float(input("\nplease input the inning of pitcher\n"))
    runners = float(input("please input the number of runners of pitcher\n"))
    whip = float(runners/inning)
    print("\nthe pitcher pitched " + str(inning) + " innings")
    print("the pitcher got " + str(runners) + " runners")
    print("the WHIP of this pitcher is "+str(whip))


while True:
    a = float(input("inning"))
