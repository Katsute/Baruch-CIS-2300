# Tuple input
# x, y = input("Enter any two values separated by a comma ',': ").split(',')

# print(x, y)

# noinspection SpellCheckingInspection
print("Chiu", "Keith", sep='\\')  # '\' escape character

# Formatting with F-Strings (string format)
print(f'{10:.4f}')          # '.4f' four decimal float
print(f'{10:.2%}')          # '.2%' two percent float
print(f'{10:.3e}')          # '.3e' 3 scientific values

name = "Aarielle"
print(f'Hello{name:25}')    # Insert variable 'name' with width of 25 spaces (no alignment).
print(f'Hello{name:<25}')   # '<' with left alignment
print(f'Hello{name:>25}')   # '>' with right alignment
print(f'Hello{name:^25}')   # '^' with center alignment

# floats are initially right aligned
age = 10.3333
print(f"Age is {age:.2f}")      # value as two decimal float
print(f"Age is {age:8,.2f}")    # value as two decimal float with width of 8 spaces

TAX_RATE = .3996784
print(f"Tax rate is {TAX_RATE:10,.2%}")

# Adaptation to last weeks assignment
print("Andrew", "${:,.2f}".format(45_400.66))
print(f"Andrew ${45_400.66:,.2f}")              # two decimal float w/comma

name, wage = "Andrew", 45_400.66
print(f"{name} ${wage:,.2f}")

