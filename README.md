
In Extra Credit: Simple Web Scraper, you use regular expressions to search the entire text of an HTML page for absolute URLs (those explicitly beginning with "http://" or "https://"). However, this misses lots of relative URLs linking to images or pages within the same domain. Let's extend the web scraper you've built so far to make sure it can also find relative URLs in <A HREF="..."> and <IMG SRC="..."> tags.

To help with this, use the HTMLparser (Links to an external site.)Links to an external site. from the standard library to explicitly recognize A and IMG tags, and access their HREF and SRC attributes. This will be in addition to the regex searches already used in your scraper. (If you prefer, you may use the Beautiful Soup library instead of HTMLparser at your discretion).

Note: you should deduplicate the urls, emails, and phone numbers found by your scraper. A set() can be an easy way to remove duplicates in a collection.