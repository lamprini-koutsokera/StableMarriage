import json
import sys

f = open(sys.argv[2], 'r')
j = json.load(f)
f.close()

men_rankings = j['men_rankings'] #the men preferences
women_rankings = j['women_rankings'] #the women preferences

free_men = list(men_rankings.keys()) #a list with the unengaged men
free_women = list(women_rankings.keys()) #a list with the unengaged women

engaged = {} #initialization of a dict with the couples

#optimal solution for men
if (sys.argv[1] == '-m'):
    #while there are unengaged-free men, the procedure continues
    while (len(free_men) is not 0):
        m = free_men.pop(0) #a first free man of a list 
        w = (men_rankings[m]).pop(0) #the man makes a proposal to his high option of his women preferences
        #if this woman is not engaged
        if w in free_women:
            engaged[m] = w #creation of the couple
            free_women.remove(w) #the woman is engaged now
        else:
            #a search for the couple at which is this woman
            for k, v in engaged.items():
                if w in v:
                    mm = k
            #if this woman prefers the current man than the previous one
            if (women_rankings[w].index(m) < women_rankings[w].index(mm)):
                engaged[m] = w #creation of the new couple
                del engaged[mm] #deletion of the previous couple
                free_men.append(mm) #addendum of the previous man at list with the unengaged men
            else:
                free_men.append(m)
    if len(sys.argv) == 5:
        if (sys.argv[3] == '-o'):
            f = open(sys.argv[4], 'w')
            json.dump(engaged, f, sort_keys=True, indent=4)
            f.close()
    else:
        j_string = json.dumps(engaged, sort_keys=True, indent=4)
        print (j_string)

#optimal solution for women
if (sys.argv[1] == '-w'):
    #while there are unengaged-free women, the procedure continues
    while (len(free_women) is not 0):
        w = free_women.pop(0) #a first free woman of a list 
        m = (women_rankings[w]).pop(0) #the woman makes a proposal to his high option of her men preferences
        #if this man is not engaged
        if m in free_men:
            engaged[w] = m #creation of the couple
            free_men.remove(m) #the man is engaged now
        else:
            #a search for the couple at which is this man
            for k, v in engaged.items():
                if m in v:
                    ww = k
            #if this man prefers the current woman than the previous one
            if (men_rankings[m].index(w) < men_rankings[m].index(ww)):
                engaged[w] = m #creation of the new couple
                del engaged[ww] #deletion of the previous couple
                free_women.append(ww) #addendum of the previous woman at list with the unengaged women
            else:
                free_women.append(w)
    if len(sys.argv) == 5:
        if (sys.argv[3] == '-o'):
            f = open(sys.argv[4], 'w')
            json.dump(engaged, f, sort_keys=True, indent=4)
            f.close()
    else:
        j_string = json.dumps(engaged, sort_keys=True,  indent=4)
        print (j_string)

