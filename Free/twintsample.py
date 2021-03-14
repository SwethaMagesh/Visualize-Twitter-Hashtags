import twint

# Configure
c = twint.Config()
c.Search = "#IPLAuction2021"
c.since="2021-02-17"
c.until="2021-02-19"

# Run
twint.run.Search(c)
