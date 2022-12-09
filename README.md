Installation:

1. `pip install -r requirements.txt`

2. Add your adventofcode.com session cookie from your browser to the `SESSION_COOKIE` variable in `settings.py` in order to fetch the `input.txt` file from adventofcode.com.

Usage:

`python new.py [year] [day]`

Creates directories and files structured in this way:
```
[year]
└───[day]
    │   [day]-1.py
    │   [day]-2.py
    │   input.txt
```

Example:

`python new.py 2022 1`