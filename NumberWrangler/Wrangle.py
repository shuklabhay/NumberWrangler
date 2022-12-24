from random import SystemRandom, choice

# Wrangler function
def Variate(number, multiplier=1, add=False, subtr=False, Round=0): ##maybe specify add or remove wrangle or have 2 funct
    # Verifying inputs
    if isinstance(number, (int, float)) and isinstance(multiplier, (int, float)) and isinstance(Round, int) and isinstance(add, bool) and isinstance(subtr, bool):

        # Math 🤓
        def addWrangle(number, multiplier, Round):
            if Round == 0:
                return(int(round((number + round((SystemRandom().uniform(0, 10)), Round) * multiplier), Round)))
            else:
                return(round((number + round((SystemRandom().uniform(0, 10)), Round) * multiplier), Round))
   
        def subtrWrangle(number, multiplier, Round):
            if Round == 0:
                return(int(round((number - round((SystemRandom().uniform(0, 10)), Round) * multiplier), Round)))
            else:
                return(round((number - round((SystemRandom().uniform(0, 10)), Round) * multiplier), Round))


        # add vs subtract
        if add == True and subtr == True:
            raise TypeError("Wrangler can not add and subtract together")
        elif add == False and subtr == False:
            if choice([0,1]) == 0:
                return(addWrangle(number, multiplier, Round))
            else:
                return(subtrWrangle(number, multiplier, Round))

        elif add == True and subtr == False: 
            return(addWrangle(number, multiplier, Round))
        elif add == False and subtr == True:
            return(subtrWrangle(number, multiplier, Round))
       

    # Verification fail
    else:
        if isinstance(number, (int, float)) == False:
            raise TypeError(f"Number input '{number}' is not valid; must be a float or int (currently {type(number)}")
        elif isinstance(multiplier, (int, float)) == False:
            raise TypeError(f"Multiplier input '{multiplier}' is not valid; must be a float or int (currently {type(multiplier)})")
        elif isinstance(Round, int) == False:
            raise TypeError(f"Rounding input '{Round}' is not valid; must be a int (currently {type(Round)})")
        elif isinstance(add, bool) == False:
            raise TypeError(f"Function input '{add}' is not valid; must be a bool (currently {type(add)})")
        elif isinstance(subtr, bool) == False:
            raise TypeError(f"Function input '{subtr}' is not valid; must be a bool (currently {type(subtr)})")
