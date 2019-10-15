# modify this function, and create other functions below as you wish
#def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
#    answer = -5
#    return answer
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    initialLevelOfDebt=float(initialLevelOfDebt)
    interestPercentage=float(interestPercentage)
    repaymentPercentage=float(repaymentPercentage)
    #print(initialLevelOfDebt)
    #print(interestPercentage)
    #print(repaymentPercentage)
    rem=float(initialLevelOfDebt)
    i=int(0)
    x=(repaymentPercentage*initialLevelOfDebt/100)
    while rem>50:
    	rem=(rem+(interestPercentage/100)*rem-(x))
    	#print(rem)
    	i=i+1
    	#print("i="+str(i))
    
    answer =int(i*(x)+(0.1*initialLevelOfDebt)+rem)
    return answer
