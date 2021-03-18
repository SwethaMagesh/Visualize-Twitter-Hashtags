with open('iplauction2.txt','r') as file:
    
    for line in file.read().split('\n'):
        field = line.split(' ')
        tweet=dict()
        if len(field)<5:
            continue
        tweet['id']=field[0]
        tweet['date']=field[1]
        tweet['time']=field[2]
        tweet['text']=' '.join(field[4:])
        
        

