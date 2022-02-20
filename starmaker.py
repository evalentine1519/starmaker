startword = input("What word do you want to star?\n").upper()
startword = startword[::-1]
middleword = startword[::-1]
middleword = middleword[1:len(middleword)]
word = startword + middleword
vertnum = range(len(word))
horiznum = range((2*len(word))-1)
#print(vertnum)
#print(horiznum)
print('word is: ' + word)

#i loop builds top to bottom
for i in vertnum:
    currentlist = []
    #j loop builds left to right
    for j in horiznum:
        #print top half
        if i < ((len(word)/2)-1):
            if j%2 == 0:
                if (j/2) == i:
                #print('one')
                    currentlist.append(word[i])
                elif (j/2) == int(len(word)/2):
                #print('two')
                    currentlist.append(word[i])
                elif (j/2) == ((len(word))-1)-i:
                #print('three')
                    currentlist.append(word[i])
                else:
                    currentlist.append(' ')
            else:
                currentlist.append(' ')
        #print midline
        elif i == int((len(word)/2)):
            if j%2 == 0:
                currentlist.append(word[int(j/2)])
            else:
                currentlist.append(' ')
        #print bottom half
        else:
            if ((j/2)+i) == (len(word)-1):
            #if (j/2) == int(len(word)/2):
                currentlist.append(word[i])
            elif (j/2) == int(len(word)/2):
                currentlist.append(word[i])
            elif (j+i) == (i*3):
                currentlist.append(word[i])
            else:
                currentlist.append(' ')
 
    print(''.join(currentlist))