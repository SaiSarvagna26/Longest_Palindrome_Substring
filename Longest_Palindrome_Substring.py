def longestPalSubstr(s):
	n=len(s)
	longest=""
	j=0
	subs=""
	subsrev=""
	for i in range(n):
		j=n-1
		while i<j:
			if(s[i]==s[j] and len(longest)<(j-i+1)):
				subs=s[i:(j+1)]
				subsrev=subs[::-1]
				if(subs==subsrev):
					longest=subs
			j-=1
	if(len(longest)==0):
		longest=s[0]
	return longest
	
if __name__ == '__main__':
	string=input()
	print(longestPalSubstr(string))

