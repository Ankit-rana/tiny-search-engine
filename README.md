# tiny-search-engine
This is implementation of a tiny search engine in Python.

This project have 3 parts:
### Crawler
This module is responsible for taking in the baseURL and crawls to other URL's associated with the baseURL until the given depth.
Also it returns the crawled websites data in the form of html file stored in the destination provided by the user.

### Indexer
This module is responsible for indexing the crawled data for the query engine to search and return the desired result.

### Query Engine
This module is responsible to take the search string as an input,look up in the indexer to return the document id and URL in descending order based on their occurance.


### Steps to execute the modules:
Crawler
sudo python crawler.py <baseURL> <Destination> <Depth>

Indexer
sudo python indexer.py <target_directory> <Output_filename>

Query Engine
sudo python queryEngine.py <Enter_string_to_be_searched> <enter_output_dat_file_of_indexer>
