for number in [12321]:
	extraction1 = number % 10 
	
extraction2 = number // 10
extraction3 = extraction2 % 10

extraction4 = extraction2 // 10
extraction5 = extraction4 % 10

extraction6 = extraction4 // 10
extraction7 = extraction6 % 10

extraction8 = extraction6 // 10
extraction9 = extraction8 % 10

if extraction1 == extraction9 and extraction3 == extraction7:
	print('12321 Is A Palindrome')
else:
	print('12321 Not A Palindrome')


