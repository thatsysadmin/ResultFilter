# thatsysadmin's Search Result Filter

This is my (very) opinionated filter list for search results. 
Feel free to have a poke around in the `domain_lists` folder.

### How does this work?
This is basically a uBlock Origin filter list generator. I basically stole the templates from `letsblock.it`
and wrote some Python (`generate_blocklists.py`) to build out the lists for me instead of having to put my 
lists in the site every single time. Easy-peasy, at least for me. The result of the Python script outputs
to `result.txt` in the root of the project directory.