import twint

# Configure
c = twint.Config()
c.Search = "(#IPLAuction2021 OR #IPL2021 OR #CSK OR #MI OR #IPLAuctions OR #RCB) until:2021-02-19 since:2021-02-17"
# Run
twint.run.Search(c)
