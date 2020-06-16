army = abs(int(input()))
if army >= 1000:
    print('legion')
elif 500 <= army <= 999:
    print('swarm')
elif 50 <= army <= 499:
    print('horde')
elif 10 <= army <= 49:
    print('pack')
elif 1 <= army <= 9:
    print('few')
else:
    print('no army')