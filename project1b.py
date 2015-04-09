import sys

def main():

    parameters=initialisation()
    
    qu_name=parameters[0]
    tw_name=parameters[1]
    bound=parameters[2]
    
    qu_list=extract_queries(qu_name)
    tw_list=extract_tweets(tw_name)

    do_approximate_matching(qu_list,tw_list,bound)

################################################################################
def initialisation():
    
    if (len(sys.argv)>1):
    #if commnad line argument is non-empty, file names are the arguments.
        if (len(sys.argv)==4):
            qu_name=sys.argv[1]
            tw_name=sys.argv[2]
            bound=int(sys.argv[3])
        else:
            print "please enter exactly 3 arguments"
            sys.exit()
    else:
        qu_name="US_small.txt"
        tw_name="training_set_tweets_small.txt"
        bound=1
    #default choices

    return [qu_name,tw_name,bound]

################################################################################
def extract_queries (FILENAME):
#extract queries from the location txt
    
    text = open(FILENAME,'r')
    loc_list=[]
    for line in text:
        data_list=line.split('\t',2)
        #only need to split twice, gain efficiency here to avoid all spliting
        loc=data_list[1]
        if ("(historical)" in loc):
            loc=loc[:len(loc)-12]
        #remove "(historical)" if exists to gain accuracy
        loc=loc.lower()
        loc_list.append(loc)
        
    loc_list=set(loc_list)
    #remove redundant items
    
    locl_final=[]
    for loc in loc_list:
        count=0
        for c in loc:
            if (c==' '):
                count+=1
    #it iterates the chars of each location to count the number of space exists
        loc_object=[loc,count]
        locl_final.append(loc_object)
    
    text.close()
    return locl_final

################################################################################
def extract_tweets(FILENAME):
    #extract tweets from the tweet txt along with their ids, lowcase them
    #and strip non-alphbetical characters

    text = open(FILENAME,'r')
    tw_list=[]
    for line in text:
        if (line[0].isdigit()!=True):
            continue
        elif ('\t' not in line):
            continue
        #mechanism for eliminating wrong stored format tweets
        
        data_list=line.split('\t')
        #separate the line to get the id and tweet string
        t_id=data_list[1]
        tw=data_list[2]

        tw=tw.strip("""~`!@#$%^&*()_-+={}|\[]:;"'<>?/,.""")
        #remove non-alphabetic charaters except for the space
        tw=tw.lower()
        tw_words=tw.split()
        
        tw_object=[tw_words,t_id]
        tw_list.append(tw_object)
    text.close()

    return tw_list

################################################################################
def do_approximate_matching(qu_list,tw_list,bound):
#do edit distance calculations
    
    for qu in qu_list:
        print "****************************************************************"
        message="""matching tweet ids for "{0}":\n""".format(qu[0])
        print message
        for tw in tw_list:
            if (qu[1]>=len(tw[0])):
                continue
            #if num of words of the query is greater than the num of tweet
            #ignore it
            for i in range(0,len(tw[0])-qu[1]):
            #loop num of words of the tweet minus the num of query plus one time
                tw_final=''
                counta=0
                for word in tw[0][i:i+qu[1]+1]:
                #select the same many words as the query
                #each time to do edit distance
                    tw_final+=word
                    counta+=1
                    if (counta<qu[1]+1):
                        tw_final+=' '
                    #a mechanism for adding appropriate spaces to the final str
                        
                dis=levenshtein(qu[0],tw_final)
                
                if (dis<=bound):
                    print tw[1]
                    break
                #print the tweet id if matchs under the boundary
        print " "
    return 0        
################################################################################
def levenshtein(s1, s2):
#copied from wikipedia code
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
 
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
 
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

################################################################################


main()
