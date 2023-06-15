def createChart(glc):
    chart = {}
    for x in glc.nonTerminals:
        chart[x] = {}
        for y in glc.terminals:
            chart[x][y] = '#' 
        chart[x]['$'] = '#' # symbol $ 
    
    #iteration to create chart
    for nonterminal in glc.productions:
        #x is the nonterminal that calls the dictionary
        productions = glc.productions[nonterminal] #this is a list of productions
        currentfirsts = glc.firstS[nonterminal] #the list of firsts from x
        for currentfirst in currentfirsts:
            #currentfirst is one first of the nonterminal X
            if(currentfirst == 'λ'):
                currentfollows = glc.followingS[nonterminal]
                for currentfollow in currentfollows:
                    chart[nonterminal][currentfollow] = 'λ'
            else: 
                foundProduction = False
                for production in productions:
                    #now production is a single production
                    listproduction = production.split() 
                    #listproduction is each symbol of a production as a list
                    donewithFirsts = False
                    n = 0 #position in production
                    while(donewithFirsts == False and production != 'λ'):
                        donewithFirsts = True 
                        productionFirsts = glc.first(listproduction[n]) 
                        for productionFirst in productionFirsts:
                            if(productionFirst != 'λ' and productionFirst == currentfirst):
                                donewithFirsts = True 
                                foundProduction = True
                                break 
                            if(productionFirst == 'λ'):
                                donewithFirsts = False 
                        n += 1
                    if(foundProduction == True):
                        #production that generates this first from nonterminal has been found
                        #the position for nonterminal and this symbol in the chart must be filled
                        #with this production
                        chart[nonterminal][currentfirst] = production 
                        break 
    return chart 

def printChart(terminals, nonterminals, chart):
    print("  ", end="")
    for x in terminals:
        print(x+"   ", end="")
    print('$')
    for x in nonterminals:
        print(x+" ", end="")
        for y in terminals:
            print(chart[x][y], end="")
            print(" ", end = "")
        print(chart[x]['$'])

def parse(sentence, chart, glc):
    #print(sentence+": ",end="")
    parsingStack = [glc.initial]
    error = False 
    if(sentence == ""):
        error = True 
    try:
        for symbol in sentence:
            character = symbol[0] #would be character in sentence.split()
            last = parsingStack.pop()
            while(character != last):
                production = chart[last][character]
                if(production == "#"):
                    error = True 
                    break
                if(production != "λ"):
                    for char in production.split()[::-1]:
                        parsingStack.append(char)
                last = parsingStack.pop()
            if(error == True):
                break
            #sentence = " ".join(sentence.split()[1:])
        
        if(len(parsingStack)>0):
        #stack still has elements
            last = parsingStack.pop()
            while(len(parsingStack) > 0 and error == False):
                production = chart[last]['$']
                if(production == "#"):
                    error = True 
                    break
                if(production != "λ"):
                    for char in production.split()[::-1]:
                        parsingStack.append(char)
                last = parsingStack.pop()

        if(error == True):
            print("Syntax error")
        else:
            print("The sentence is syntactically correct.")

    except:
        print("Syntax error")
    

def differentFirstandFollowing(firsts, followings):
    different = True
    for x in firsts:
        firstset = set(firsts[x])
        followingset = set(followings[x])
        if(firstset & followingset):
            different = False 
            print("Nonterminal with repeated elements: "+x)
            print("Firsts: ",firstset)
            print("Followings: ",followingset)
            break 
    return different 







                

            

        
    

