
# A simple tool to copy a YouTube Channel to a Google Map

Setup:

    copy config-dist.py config.py

Add your play list ID and Google API key to `config.py`

Then load your videos:

    python3 chanload.py

Then produce the JSON

    python3 chandump.py

Then open `index.htm` making sure to clear cache

