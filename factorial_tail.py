def count_divisor(prime, number):
    count = 0
    while number % prime == 0:
        number = number / prime
        count += 1
    return count

def get_primes_until(number):
    primes = []
    for n in range(2, int(number)+1):
        is_prime = True
        for prime in primes:
            if n % prime == 0:
                is_prime = False
        
        if is_prime:
            primes.append(n)
    return primes

def express_in_primes(number):
    primes = []
    primes_times = []
    all_primes = get_primes_until(number)
    for candidate in all_primes:
        if count_divisor(candidate, number) > 0:
            primes.append(candidate)
            primes_times.append(count_divisor(candidate, number))
        else:
            continue
    
    return primes, primes_times
        

def zeroes(base, number):
    print(base, number)
    primes, primes_times = express_in_primes(base)
    primes_count = [0] * len(primes)
    for n in range(1, number + 1):
        for i,prime in enumerate(primes):
            if n % prime == 0:
                primes_count[i] += count_divisor(prime, n)
    for i in range(len(primes)):
        primes_count[i] = primes_count[i] // primes_times[i]
                
    return min(primes_count)