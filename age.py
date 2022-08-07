drive = input('請問你有沒有開過車？')
if drive != '有' and drive != '無':
	print ('別鬧了')
	raise SystemExit
age = input('請問你的年齡：')
age = int(age)
if drive == '有':
	if age >= 18:
		print('你通過測驗')
	else:
		print('bad dog')
elif drive == '沒有':
	if age >= 18:
		print('考駕照')
	else:
		print('繼續等')