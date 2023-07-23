# Import Package
from NumberWrangler import Wrangler

# Create a Variate object
Variate = Wrangler.Variate

# Create a number close to 12
print(Variate(number=12))

# Create a number far from 12
print(Variate(number=12, multiplier=200))

# Create a number close to 12 rounded to the fifth place
print(Variate(number=12, round=5))

# Create a number close to but more than 12
print(Variate(number=12, add=True))

# Create a number close to but less than 12
print(Variate(number=12, subtr=True))

# Now use any combination of these methods!
# Generates a new number after each use.