
class ScubaTank:
    # Problem 4 code here
    ...


# Problem 5 
def transfer_air(source, target, amount):
    old = source.get_bar()
    source.release(amount)

    if amount > 0 and source.get_bar() == old - amount:
        target.fill(amount)

