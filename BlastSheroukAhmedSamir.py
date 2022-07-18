#رنين خالد محمد
#شروق أحمد سمير
#روان السيد توفيق
#مريم حسن ابراهيم
#ايمان وجيه رفيق
#منة الله حمدي مصطفي

import sys
blosum62 ={
    'C':{'C':9, 'S':-1, 'T':-1, 'P':-3, 'A':0,  'G':-3, 'N':-3, 'D':-3, 'E':-4, 'Q':-3, 'H':-3, 'R':-3, 'K':-3, 'M':-1, 'I':-1, 'L':-1, 'V':-1, 'F':-2, 'Y':-2, 'W':-2},
    'S':{'C':-1,'S':4,  'T':1,  'P':-1, 'A':1,  'G':0,  'N':1,  'D':0,  'E':0,  'Q':0,  'H':-1, 'R':-1, 'K':0,  'M':-1, 'I':-2, 'L':-2, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'T':{'C':-1,'S':1,  'T':4,  'P':1,  'A':-1, 'G':1,  'N':0,  'D':1,  'E':0,  'Q':0,  'H':0,  'R':-1, 'K':0,  'M':-1, 'I':-2, 'L':-2, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'P':{'C':-3,'S':-1, 'T':1,  'P':7,  'A':-1, 'G':-2, 'N':-1, 'D':-1, 'E':-1, 'Q':-1, 'H':-2, 'R':-2, 'K':-1, 'M':-2, 'I':-3, 'L':-3, 'V':-2, 'F':-4, 'Y':-3, 'W':-4},
    'A':{'C':0, 'S':1,  'T':-1, 'P':-1, 'A':4,  'G':0,  'N':-1, 'D':-2, 'E':-1, 'Q':-1, 'H':-2, 'R':-1, 'K':-1, 'M':-1, 'I':-1, 'L':-1, 'V':-2, 'F':-2, 'Y':-2, 'W':-3},
    'G':{'C':-3,'S':0,  'T':1,  'P':-2, 'A':0,  'G':6,  'N':-2, 'D':-1, 'E':-2, 'Q':-2, 'H':-2, 'R':-2, 'K':-2, 'M':-3, 'I':-4, 'L':-4, 'V':0,  'F':-3, 'Y':-3, 'W':-2},
    'N':{'C':-3,'S':1,  'T':0,  'P':-2, 'A':-2, 'G':0,  'N':6,  'D':1,  'E':0,  'Q':0,  'H':-1, 'R':0,  'K':0,  'M':-2, 'I':-3, 'L':-3, 'V':-3, 'F':-3, 'Y':-2, 'W':-4},
    'D':{'C':-3,'S':0,  'T':1,  'P':-1, 'A':-2, 'G':-1, 'N':1,  'D':6,  'E':2,  'Q':0,  'H':-1, 'R':-2, 'K':-1, 'M':-3, 'I':-3, 'L':-4, 'V':-3, 'F':-3, 'Y':-3, 'W':-4},
    'E':{'C':-4,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':2,  'E':5,  'Q':2,  'H':0,  'R':0,  'K':1,  'M':-2, 'I':-3, 'L':-3, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'Q':{'C':-3,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':0,  'E':2,  'Q':5,  'H':0,  'R':1,  'K':1,  'M':0,  'I':-3, 'L':-2, 'V':-2, 'F':-3, 'Y':-1, 'W':-2},
    'H':{'C':-3,'S':-1, 'T':0,  'P':-2, 'A':-2, 'G':-2, 'N':1,  'D':1,  'E':0,  'Q':0,  'H':8,  'R':0,  'K':-1, 'M':-2, 'I':-3, 'L':-3, 'V':-2, 'F':-1, 'Y':2,  'W':-2},
    'R':{'C':-3,'S':-1, 'T':-1, 'P':-2, 'A':-1, 'G':-2, 'N':0,  'D':-2, 'E':0,  'Q':1,  'H':0,  'R':5,  'K':2,  'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'K':{'C':-3,'S':0,  'T':0,  'P':-1, 'A':-1, 'G':-2, 'N':0,  'D':-1, 'E':1,  'Q':1,  'H':-1, 'R':2,  'K':5,  'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':-3, 'Y':-2, 'W':-3},
    'M':{'C':-1,'S':-1, 'T':-1, 'P':-2, 'A':-1, 'G':-3, 'N':-2, 'D':-3, 'E':-2, 'Q':0,  'H':-2, 'R':-1, 'K':-1, 'M':5,  'I':1,  'L':2,  'V':-2, 'F':0,  'Y':-1, 'W':-1},
    'I':{'C':-1,'S':-2, 'T':-2, 'P':-3, 'A':-1, 'G':-4, 'N':-3, 'D':-3, 'E':-3, 'Q':-3, 'H':-3, 'R':-3, 'K':-3, 'M':1,  'I':4,  'L':2,  'V':1,  'F':0,  'Y':-1, 'W':-3},
    'L':{'C':-1,'S':-2, 'T':-2, 'P':-3, 'A':-1, 'G':-4, 'N':-3, 'D':-4, 'E':-3, 'Q':-2, 'H':-3, 'R':-2, 'K':-2, 'M':2,  'I':2,  'L':4,  'V':3,  'F':0,  'Y':-1, 'W':-2},
    'V':{'C':-1,'S':-2, 'T':-2, 'P':-2, 'A':0,  'G':-3, 'N':-3, 'D':-3, 'E':-2, 'Q':-2, 'H':-3, 'R':-3, 'K':-2, 'M':1,  'I':3,  'L':1,  'V':4,  'F':-1, 'Y':-1, 'W':-3},
    'F':{'C':-2,'S':-2, 'T':-2, 'P':-4, 'A':-2, 'G':-3, 'N':-3, 'D':-3, 'E':-3, 'Q':-3, 'H':-1, 'R':-3, 'K':-3, 'M':0,  'I':0,  'L':0,  'V':-1, 'F':6,  'Y':3,  'W':1},
    'Y':{'C':-2,'S':-2, 'T':-2, 'P':-3, 'A':-2, 'G':-3, 'N':-2, 'D':-3, 'E':-2, 'Q':-1, 'H':2,  'R':-2, 'K':-2, 'M':-1, 'I':-1, 'L':-1, 'V':-1, 'F':3,  'Y':7,  'W':2},
    'W':{'C':-2,'S':-3, 'T':-3, 'P':-4, 'A':-3, 'G':-2, 'N':-4, 'D':-4, 'E':-3, 'Q':-2, 'H':-2, 'R':-3, 'K':-3, 'M':-1, 'I':-3, 'L':-2, 'V':-3, 'F':1,  'Y':2,  'W':11}
   }

def low_complexity(querySequence):
    print("The Query you write : " + querySequence)
    repl_dict = {'C':'X'
        ,'S':'X'
        , 'T':'X'
        , 'P':'X'
        , 'A':'X'
        , 'G':'X'
        , 'N':'X'
        , 'D':'X'
        , 'E':'X'
        , 'Q':'X'
        , 'H':'X'
        , 'R':'X'
        , 'K':'X'
        , 'M':'X'
        , 'I':'X'
        , 'L':'X'
        , 'V':'X'
        , 'F':'X'
        ,'Y':'X'
        , 'W':'X'}
    for i, c in enumerate(querySequence[:-1]):  # i is the current index, c is the current char
        if querySequence[i + 1] == c:
         duplicates = []
         for char in querySequence:
          if querySequence.count(char) > 1:
            for i, j in repl_dict.items():
              querySequence = querySequence.replace(char, j)
              # appending to the list if it's already not present
            for i, c in enumerate(querySequence[:-1]):  # i is the current index, c is the current char
                if querySequence[i + 1] == c:
                  if char not in duplicates:
                    duplicates.append(char)
    print("The Query after low comlexity : " + querySequence)

def query_to_word(querySequence,n):
    arr = []
    for i in range(0, len(querySequence)):
        if len(querySequence[i:i + n]) < n:
         continue
        else:
         slic = slice(i, i + n, 1)
         arr.append(querySequence[slic])
    return (arr)

def neighborhood_words(arr, T):
        amino_acids = ['A', ',R', 'N', 'D', 'C', 'E', 'G', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y','V']
        neighborhoodWord=[]
        scoree=[]
        seeds = []
        for i in range(len(arr)):
             for j in range(len(arr[i])):
                 for z in range(len(amino_acids)):
                     score=0
                     new = arr[j].replace(arr[i][j], amino_acids[z])
                     # print("word:", arr[i], "new:", new, "score:", score)
                     if len(new) == 3:
                       neighborhoodWord.append(new)
                       for x in range(len(new)):
                          score += blosum62[new[x]][arr[i][x]]
                       if score >= T:
                          seeds.append(new)
                          scoree.append(score)
        return scoree,neighborhoodWord,seeds

def DatabaseSequence(filename):
    file=open('Protein.TXT')
    Database=[]
    for line in file:
        Database.append(line.rstrip())
    file.close()
    return Database

def wordHitting(Database ,seeds):
    wordhitIndex=[]
    for i in range(len(seeds)):
        for j in range(len(Database)):
             if seeds[i][0] in Database[j]:
                  databaseIndex=Database[j].find(seeds[i][0])
                  wordhitIndex.append((seeds[i],j,databaseIndex,seeds[i]))
    return wordhitIndex

def Extend(hits,querySequence,Database,TS):
    HSP = []

    for i in range (len(hits)):
        finalSEQ = ""
        finalDb = ""
        count = 1
        oldscore = 0
        newscore = 0
        forword = 0
        backword = 0

        maxcount = 0
        if len(querySequence) < len(Database):
            minlen = len(querySequence)
            forword = minlen - 3 - (hits[i][0])
            backword = len(querySequence) - 3 - forword
            maxcount = min(forword,backword)
        elif len(Database[hits[i][1]]) < len(querySequence):
            minlen = len(Database[hits[i][1]])
            forword = minlen - 3 - (hits[i][2])
            backword = len(Database[hits[i][1]]) - 3 - forword
            maxcount = min(forword,backword)



        sindex = hits[i][0]
        dseq = Database[hits[i][1]]
        dindex = hits[i][2]
        query = hits[i][3]
        dbbbb = dseq[dindex:dindex + 3]
        finalSEQ += query
        finalDb += dbbbb
        noextend=[]
        for k in range(len(hits[i][3])):
            oldscore += blosum62[query[k]][dbbbb[k]]


        if maxcount == 0:

            if forword == 0 and backword == 0:
               if(oldscore >= TS):
                HSP.append((query,dbbbb,oldscore,noextend))

            elif forword > 0 and backword == 0:
                countf = 0
                newscore += oldscore
                for a in range(forword):

                    queryword = querySequence[sindex + 3 + countf]

                    dbword = dseq[dindex + 3 + countf]


                    newscore += blosum62[queryword][dbword]
                    if newscore < oldscore:
                        HSP.append((finalSEQ, finalDb, oldscore,"f"))
                        continue

                    else:
                        finalSEQ += queryword
                        finalDb += dbword
                        oldscore = newscore

                    countf += 1
                HSP.append((finalSEQ, finalDb, newscore))

            elif forword == 0 and backword > 0:
                countb = 0
                newscore += oldscore
                for j in range(backword):

                    queryword = querySequence[sindex - countb]

                    dbword = dseq[dindex - countb]

                    newscore += blosum62[queryword][dbword]
                    if newscore < oldscore:
                        finalSEQ += query
                        finalDb += dbbbb
                        HSP.append((finalSEQ, finalDb, newscore))
                        continue

                    else:
                        finalSEQ += queryword
                        finalDb += dbword
                        oldscore = newscore

                    countb += 1



        elif maxcount>0:
            for j in range(maxcount):

                sindex = hits[i][0]

                queryword = querySequence[sindex - count]
                queryword += query
                queryword += querySequence[sindex+2+count]
                dbword = dseq[dindex - count]
                dbword += dbbbb
                dbword += dseq[dindex+2+count]


                for l in range(len(dbword)):
                    newscore += blosum62[queryword[l]][dbword[l]]
                if newscore < oldscore:
                    HSP.append((finalSEQ,finalDb,oldscore))
                    continue

                else:
                    HSP.append((queryword,dbword,newscore))

                count += 1
    return HSP


#######################################
#####MAIN########
print('Enter your protein query sequence: ')
querySequence=input()


print ( 'enter word threshold: ')
T=input()
T = int(T)


print ( 'enter word lenght: ')
n=input()
n = int(n)


print ( 'enter HSPS threshold: ')
TS=input()
TS = int(TS)




arr = query_to_word(querySequence,n)
print("words of query  " + querySequence+' :')
print(arr)
scoree,neighborhood,seeds=neighborhood_words(arr,T)
print("before threshold neighborhood:")
print(neighborhood)
print("after threshold seeds:")
print(seeds)
print("score:")
print(scoree)






low_complexity(querySequence)
Database=DatabaseSequence("Protein.TXT")
hits=wordHitting(Database,seeds)
print('Hits: ')
print(hits)

Hsps = Extend(hits,querySequence,Database,TS)
print('Hsps: ')
print(Hsps)