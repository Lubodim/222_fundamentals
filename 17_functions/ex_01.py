def calc(num, power):
    return f"{num} to the power of {power} = {num**power}"


n = list(map(int, input().split(", ")))
calc(n[0], n[1])
