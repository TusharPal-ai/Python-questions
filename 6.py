l=["tushar","tulsi","harshi","gupta","tandon"]
def rem(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n

print(rem(l,"an"))
