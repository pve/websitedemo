import html5lib
#with open("index.html", "rb") as file
with open("styles.css", "rb") as f:
    parser = html5lib.HTMLParser(strict=True)
    document = parser.parse(f)
    
    # https://validator.w3.org/check?uri=https://example.com/&output=json