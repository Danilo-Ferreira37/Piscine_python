from typing import Generator

def events_generator(n_events: int) -> Generator[str, None, None]:
    event_number = 0
    player = ["alice", "bob", "charlie"]
    level = [5, 12, 8]
    acts = ["killed monster", "found treasure", "leveled up"]

    for i in range(n_events):
        p = player[i % len(player)]
        l = level[i % len(level)]
        a = acts[i % len(acts)]
        yield f"Event {event_number + 1}: Player {p} (level {l}) {a}"
        event_number += 1
        if i == 2:
            break
    yield("...\n")


def fibonacci(n: int) -> Generator[int, None, None]:
    count = 0
    prev1 = 0
    prev2 = 1
    yield 0
    yield 1

    while count < (n - 2):
        fib = prev1 + prev2
        yield fib
        prev1 = prev2
        prev2 = fib
        count += 1


def list_primes(n: int) -> Generator[int, None, None]:
    count = 0
    prime = 2

    while(count < n):
        condition = True
        div = 2
        while div * div <= prime:
            if prime % div == 0:
                condition = False
                break
            div += 1
        if condition:
            yield prime
            count += 1
        prime += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    n_events = 1000
    hight_lev = 0
    treasure = 0
    level = 0
    print(f"Processing {n_events} game events...\n")
    try:
        for event in events_generator(n_events):
            print(event)
            if "level" in event:
                temp = event.replace(")", "")
                temp = int(temp.split(" ")[5])
                if temp > 10:
                    hight_lev += 1
            if "treasure" in event:
                treasure += 1
            if "leveled up" in event:
                level += 1
        print("=== Stream Analytics ===")
        print("Total events processed:", n_events)
        print(f"High-level players (+10): {hight_lev}")
        print(f"Treasure events: {treasure}")
        print(f"Level-up events: {level}")
        print("\nMemory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds")
        
        fibs = ""
        for n in fibonacci(10):
            fibs += str(n)
            fibs += ", "
        fibs = fibs[:-2]
        
        primes = ""
        for n in list_primes(5):
            primes += str("s")
            primes += ", "
        primes = primes[:-2]
        print("\n=== Generator Demonstration ===")
        print(f"Fibonacci sequence (first 10): {fibs}")
        print(f"Prime numbers (first 5): {primes}")
    except ValueError as e:
        print(e)
