sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = sum(sentence.count('капитан') for sentence in sentences)
print(cap_count)
