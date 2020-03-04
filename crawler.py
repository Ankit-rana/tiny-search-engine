from util import get_content,find_links,write_content
import sys
import asyncio

URLList = []
COUNT = 0

async def main():
    global COUNT
    if len(sys.argv) != 4:
        print("Wrong info passed")
        sys.exit(1)

    baseurl = sys.argv[1]
    destination = sys.argv[2]
    depth = int(sys.argv[3])

    URLList.append(baseurl)

    # TODO: make each iteration as task
    for link in URLList:
        if not link.startswith('http'):
            continue
        ## get the html page
        ## made it async because this requires IO bound work ie. get data over network
        ## common mistake:
        ## $ python3.7 crawler.py 
        ## File "crawler.py", line 26
        ## await data = get_content(link)
        ## ^
        ## SyntaxError: can't assign to await expression

        data = await get_content(link)

        ## find out the links in the page and add it to a list
        ## avoided to make this async because this is not a IO bound work
        find_links(data, URLList) if depth > 0 else sys.exit(1)

        ## print in the file (url,depth,content)
        ## avoided this due to lack of asyncio in linux 
        ## https://stackoverflow.com/questions/87892/what-is-the-status-of-posix-asynchronous-i-o-aio
        COUNT = write_content(link, str(depth), data, destination, COUNT)

        ## depth--
        depth -= 1

if __name__ == "__main__":
    asyncio.run(main())

