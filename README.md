# NumberWrangler

**Variate** numbers!

## Instructions

1. Install:

```
pip install NumberWrangler
```

2. Variate numbers

```python
# Import Package
from NumberWrangler import Wrangler

#Create a Variate object for simplicity
Variate = Wrangler.Variate

# Variate a number close to 12
print(Variate(number=12))
```

3. Success!

## Documentation and Examples

```python
# Variate a number close to 12
print(Variate(number=12))

# Variate a number far from 12
print(Variate(number=12, multiplier=200))

# Variate a number close to 12 that is a float
print(Variate(number=12, Round=5))

# Variate a number close to 12 that is adding
print(Variate(number=12, add=True))

# Variate a number close to 12 that is subtracting
print(Variate(number=12, subtr=True))

# Variate a number close to 12 that is subtracting
print(Variate(number=12, subtr=True))

# Now use any combination of these methods!
```
