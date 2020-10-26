xy = 0
while xy < 50:

    ENTH = float(input("Voter Enthusiasm (I/R): "))
 
    RP = float(input("Polling (R): ")) 
    DP = float(input("Polling (D): ")) 


    PRV = 15.1 + (0.73*RP) + (0.01*ENTH)
    PDV = 23.1 - (0.04*ENTH) + (0.53*DP)

    if (PRV+PDV) > 100:
        PRV = 100 - PDV



    print("All Margins are for (R)")
    print("")



    WI  = ""
    PA  = ""
    MN  = ""
    IA  = ""
    OH  = ""
    NH  = ""
    ME  = ""
    VA  = ""
    NC  = ""
    GA  = ""
    FL  = ""
    TX  = ""
    NM  = ""
    CO  = ""
    AZ  = ""
    NV  = ""
    OR  = ""

    



    MA = PRV - PDV
  
    
    MI = -1.4209 + (0.82158*(-1)) + (0.57467*MA)

    WI = -1.4209 + (0.82158*(1)) + (0.57467*MA)

    PA = -1.4209 + (0.82158*(1)) + (0.57467*MA)

    MN = -1.4209 + (0.82158*(-2)) + (0.57467*MA)

    IA = -1.4209 + (0.82158*(6)) + (0.57467*MA)

    OH = -1.4209 + (0.82158*(7)) + (0.57467*MA)

    NH = -1.4209 + (0.82158*(2)) + (0.57467*MA)

    ME = -1.4209 + (0.82158*(-5)) + (0.57467*MA)

    VA = -1.4209 + (0.82158*(-5)) + (0.57467*MA)

    NC = -1.4209 + (0.82158*(2)) + (0.57467*MA)

    SC = -1.4209 + (0.82158*17) + (0.57467*MA)

    GA = -1.4209 + (0.82158*(12)) + (0.57467*MA)

    FL = -1.4209 + (0.82158*(5)) + (0.57467*MA)

    TX = -1.4209 + (0.82158*(17)) + (0.57467*MA)

    NM = -1.4209 + (0.82158*(-7)) + (0.57467*MA)

    CO = -1.4209 + (0.82158*(-1)) + (0.57467*MA)

    AZ = -1.4209 + (0.82158*(9)) + (0.57467*MA)
    
    NV = -1.4209 + (0.82158*(1)) + (0.57467*MA)

    OR = -1.4209 + (0.82158*(-9)) + (0.57467*MA)


    print("MI: " + str(MI))
    print("WI: " + str(WI))
    print("PA: " + str(PA))
    print("MN: " + str(MN))
    print("IA: " + str(IA))
    print("OH: " + str(OH))
    print("NH: " + str(NH))
    print("ME: " + str(ME))
    print("VA: " + str(VA))
    print("NC: " + str(NC))
    print("GA: " + str(GA))
    print("FL: " + str(FL))
    print("TX: " + str(TX))
    print("NM: " + str(NM))
    print("CO: " + str(CO))
    print("AZ: " + str(AZ))
    print("NV: " + str(NV))
    print("OR: " + str(OR))



    print("Popular Vote: " + "Republican: " + str(PRV) + ", Democrat: " + str(PDV))
    print("For each state, if polling is available, multiply the margin of the average by 0.13, and at that to the total.")
    print("")
    xy=xy+1    
