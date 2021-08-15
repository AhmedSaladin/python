# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print((23 + 32 + 64) / 3)


# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling.
# One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.
# How many tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

# Fill this in with an expression that calculates how many tiles are needed.
print((5 * 7) + (9 * 7))

# Fill this in with an expression that calculates how many tiles will be left over.
print((17 * 6) - (5 * 7 + 9 * 7))

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5 

# print the new value of the reservoir_volume variable
print(reservoir_volume)
