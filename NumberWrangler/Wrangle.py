from random import SystemRandom, choice

# Wrangler function
def Variate(number, multiplier=1, add=False, subtr=False, round=0):

    if (
        isinstance(number, (int, float))
        and isinstance(multiplier, (int, float))
        and isinstance(round, int)
        and isinstance(add, bool)
        and isinstance(subtr, bool)
    ):

        def addWrangle(number, multiplier, round):
            if round == 0:
                return int(
                    round(
                        (
                            number
                            + round((SystemRandom().uniform(0, 10)), round) * multiplier
                        ),
                        round,
                    )
                )
            else:
                return round(
                    (
                        number
                        + round((SystemRandom().uniform(0, 10)), round) * multiplier
                    ),
                    round,
                )

        def subtrWrangle(number, multiplier, round):
            if round == 0:
                return int(
                    round(
                        (
                            number
                            - round((SystemRandom().uniform(0, 10)), round) * multiplier
                        ),
                        round,
                    )
                )
            else:
                return round(
                    (
                        number
                        - round((SystemRandom().uniform(0, 10)), round) * multiplier
                    ),
                    round,
                )

        if add == True and subtr == True:
            raise TypeError("Wrangler can not add and subtract together")
        elif add == False and subtr == False:
            if choice([0, 1]) == 0:
                return addWrangle(number, multiplier, round)
            else:
                return subtrWrangle(number, multiplier, round)

        elif add == True and subtr == False:
            return addWrangle(number, multiplier, round)
        elif add == False and subtr == True:
            return subtrWrangle(number, multiplier, round)

    # Verification fail
    else:
        if isinstance(number, (int, float)) == False:
            raise TypeError(
                f"Number input '{number}' is not valid; must be a float or int (currently {type(number)}"
            )
        elif isinstance(multiplier, (int, float)) == False:
            raise TypeError(
                f"Multiplier input '{multiplier}' is not valid; must be a float or int (currently {type(multiplier)})"
            )
        elif isinstance(round, int) == False:
            raise TypeError(
                f"rounding input '{round}' is not valid; must be a int (currently {type(round)})"
            )
        elif isinstance(add, bool) == False:
            raise TypeError(
                f"Function input '{add}' is not valid; must be a bool (currently {type(add)})"
            )
        elif isinstance(subtr, bool) == False:
            raise TypeError(
                f"Function input '{subtr}' is not valid; must be a bool (currently {type(subtr)})"
            )
