import itertools

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm

        # M cannot be zero (leading digit of MONEY)
        if m == 0 or s == 0:
            continue

        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 + y

        if send + more == money:
            print("Solution Found!")
            print(f"SEND  = {send}")
            print(f"MORE  = {more}")
            print(f"MONEY = {money}")
            print(f"Mapping: S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
            return  # stop after first solution

solve_cryptarithmetic()
