import twint

# Configure
c = twint.Config()
c.Search = "-#IPLAuction2021 -#IPL2021 -#CSK -#MI -#RCB -#IPLAuctions (#IPlAuction2021live OR #Yellove OR #WhistlePodu OR #MumbaiIndians OR #YehHaiNayiDilli OR #WeRoarTogether OR #OrangeArmy OR #PunjabKings OR #RisersRetained OR #Sachin OR #ArjunTendulkar OR #SachinBaby OR #Pujara OR #GlennMaxwell) until:2021-02-19 since:2021-02-17"
# Run
twint.run.Search(c)
