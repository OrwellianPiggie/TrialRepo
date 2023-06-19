if __name__=='__main__':
	n=int(input())
	stamps=list(map(lambda _:input(),range(n)))
	sett=set()
	for i in range(n):
		sett.add(stamps[i])
	print(len(sett))	