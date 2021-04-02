import twint

# Configure
c = twint.Config()
c.Search = "(#IPLAuction2021live OR #IPLAuctions2021 OR #IPL OR #IPL2021 OR #IPL OR #Auction OR # OR IPL2021Auctions OR #IPLAuctions OR #Cricket OR or OR #VIVOIPLAuction OR #IPLRetention OR #whistlepodu OR #yellove OR #Onefamily OR #MumbaiIndians OR #WeRoarTogether OR #YeyHaiNayiDilli OR #DelhiCapitals)  until:2021-02-19 since:2021-02-17"

#Second
#c.Search="(#OrangeArmy OR #RisesRetained OR #MoeenAli OR #ArjunTendulkar OR #Nepotism OR #ShahrukhKhan OR #SachinTendulkar OR #MSDhoni OR #SanjuSamson OR #SteveSmith OR #RishabPant OR #Nepokid OR #SachinBaby) until:2021-02-19 since:2021-02-17"
#Third 
#c.Search="(#CSI OR #MI OR #KKR OR #DC OR #RCB OR #KXIP OR #SRH OR #RR) until:2021-02-19 since:2021-02-17"
#Fourth
#c.Search="(#sunrisesHyderabad OR #cricketlover OR #jadega OR #cricketmerijaan OR #maxwell OR #bumrah OR #ajinkyarahane OR #indianpremierleague OR #BCCI OR #viratkohli OR #TuneinNow OR #SuperAuction  OR #latestcricketnewsinhindi OR #krishnappaGowtham OR #AuctionDay OR #CricbuzzLive) until:2021-02-19 since:2021-02-17"

twint.run.Search(c)


