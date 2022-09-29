#Sieve of Eratosthenens

integers = list(x for x in range(2, 1001))

for current_prime in integers:
    for prime_multiple in range(current_prime*2, 1001, current_prime):
        if prime_multiple in integers:
            integers.remove(prime_multiple)

print(integers)
print(len(integers))