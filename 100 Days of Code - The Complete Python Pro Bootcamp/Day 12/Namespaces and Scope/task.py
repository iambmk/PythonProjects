# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

player_health = 100

def drink_portion():
    portion_strength = 2
    print(player_health)

drink_portion()
print(player_health)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Testing the function
num = 10
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

