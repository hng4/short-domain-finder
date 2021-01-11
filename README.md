# short-domain-finder
Find short domains under a specified TLD.

Run using
```
python3 find.py
```
It'll dump all domains which have a slight error, when it's finished open results.txt and there will be a list of 2 letter domains. It uses the list.txt file which contains all 2 letter combinations

# Change the TLD?
Edit the below line in the python file and re-run.
```
TLD="mytld"
```
It gathers all NXDOMAIN's, Sometimes it glitches.
