f = open('ums_numbers.txt', 'w')
perfectum = open('perfectum_numbers.txt', 'w')
beeline = open('beeline.txt', 'w')
uzmobile = open('uzmobile.txt', 'w')
ucell = open('ucell.txt', 'w')


f.write("start\n")
perfectum.write("start\n")
beeline.write("start\n")
uzmobile.write("start\n")
ucell.write("start\n")

for i in range(1000000,9999999):
	f.write(f"97{i}\n")
	perfectum.write(f"98{i}\n")
	beeline.write(f"90{i}\n")
	uzmobile.write(f"99{i}\n")
	ucell.write(f"93{i}\n")






f.close()
