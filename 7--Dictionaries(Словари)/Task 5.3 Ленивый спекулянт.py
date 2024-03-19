rates = {'Sberbank': 55.8, 'VTB24': 53.91}

best_bank = min(rates, key=rates.get) # Find a key with minimal value
best_rate = rates[best_bank]
print(f'Bank: {best_bank} --> {best_rate}')

input()