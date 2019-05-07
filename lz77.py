#!/usr/bin/python


def lz77(string,size_of_lab=5,size_of_sb=5):
	ans = []
	# initialize search_buffer and look_ahead_buffer
	search_buffer = []
	look_ahead_buffer = []
	print search_buffer,look_ahead_buffer
	# string fill up in look_ahead_buffer list
	for i in range(0,size_of_lab):
		look_ahead_buffer.append(string[i])
	print search_buffer,look_ahead_buffer
	# initial phase 0
	if len(search_buffer) == 0:
		search_buffer.append(look_ahead_buffer[0])
		m = look_ahead_buffer[0]
		del look_ahead_buffer[0]
		look_ahead_buffer.append(string[i+1])
		i += 1
		print search_buffer,look_ahead_buffer,"No Match of",m,"<%s ,%s, C(%s)>"%(0,0,m)
		ans.append("<%s ,%s, C(%s)>"%(0,0,m))
	# phase 1
	for j in range(0,len(string)-1):
		try:
			if look_ahead_buffer[0] in search_buffer:
				match = []
				c = 0
				u = []
				d = {}
				non_ans = []
				for k in search_buffer:
					if look_ahead_buffer[0] == k:
						match.append(c)
					c += 1
				for x in match:
					z = 1
					non_ans_string = search_buffer[x]
					for y in range(0,len(search_buffer)):
						try:
							if search_buffer[x+y+1] == look_ahead_buffer[y+1]:
								non_ans_string += search_buffer[x+y+1]
								z += 1
							else:
								break
						except:
							for v in range(len(look_ahead_buffer)):
								try:
									if look_ahead_buffer[v] == look_ahead_buffer[y+1]:
										non_ans_string += look_ahead_buffer[v]
										z += 1
										y += 1
									else:
										break
								except:
									pass
					non_ans.append(non_ans_string)
					d[z] = x
					u.append(z)
				u.sort()
				max = u[len(u)-1]
				offset = len(search_buffer[d[max]:])
				for p in range(max+1):	
					if len(search_buffer) == size_of_sb:
						del search_buffer[0]
					search_buffer.append(look_ahead_buffer[0])
					m = look_ahead_buffer[0]
					del look_ahead_buffer[0]
					try:
						look_ahead_buffer.append(string[i+1])
					except:
						pass
					i += 1
				print search_buffer,look_ahead_buffer,match,u,
				for q in non_ans:
					print non_ans,
				print "<%s ,%s, C(%s)>"%(offset,max,m)
				ans.append("<%s ,%s, C(%s)>"%(offset,u[len(u)-1],m))
			else:
				if len(search_buffer) == size_of_sb:
					del search_buffer[0]
				search_buffer.append(look_ahead_buffer[0])
				m = look_ahead_buffer[0]
				del look_ahead_buffer[0]
				try:
					look_ahead_buffer.append(string[i+1])
				except:
					pass
				i += 1
				ans.append("<%s ,%s, C(%s)>"%(0,0,m))
				print search_buffer,look_ahead_buffer,
				print "No Match of",m,"<%s ,%s, C(%s)>"%(0,0,m)
		except IndexError:
			break
	print "\nAnswer :",search_buffer,look_ahead_buffer
	print '\nCodeWord :',
	for i in ans:
		print i,'\n\t  ',
	print ''
	print "Encoding LZ77 Complete."



if __name__ == "__main__":
	string = raw_input("Enter String : ")
	sb = raw_input("Enter Search Buffer Size (Optional) : ")
	lab = raw_input("Enter Look Ahead Buffer Size (Optional) : ")
	try:
		sb = int(sb)
	except:
		pass
	try:
		lab = int(lab)
	except:
		pass
	if type(sb) == type(7) and type(lab) == type(7):
		string += '.,'
		print "Start Encoding..."
		lz77(string,lab,sb)#cabracadabrarrarrad")#,int(lab),int(sb))#"cabracadabrarrarrad",6,7)#)string,int(lab),int(sb))#abaraabraa")#"abaraabraa")#cabracadabrarrarrad")#abaraabraa.,")#"cabracadabrarrarrad",6,7)#abaraabraa")#string,lab,sb)
	elif type(sb) == type(7) and type(lab) != type(7):
		string += '.,'
		print "Start Encoding..."
		lz77(string,size_of_sb=sb)
	elif type(lab) == type(7) and type(sb) != type(7):
		string += '.,'
		print "Start Encoding..."
		lz77(string,size_of_lab=lab)
	else:
		string += '.,'
		print "Start Encoding..."
		lz77(string)

	raw_input("press any key to exit...")