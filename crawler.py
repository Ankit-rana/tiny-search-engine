from util import get_content,find_links,write_content
import sys
import asyncio

URLList = []
COUNT = 0

async def url_logic(url,i,depth, destination):
    urls = []
    if i == depth:
        return
    if not url:
        return
    if not url.startswith('http'):
        return
    ## get the html page
    print("%s step1"%url)
    data = await get_content(url)

    ## find out the links in the page and add it to a list
    print("%s step2"%url)
    find_links(data, urls) if depth > 0 else sys.exit(1)

    ## print in the file (url,depth,content)
    global COUNT
    print("%s step3"%url)
    COUNT = write_content(url, str(depth), data, destination, COUNT)

    tasks = []
    for u in urls:
        tasks.append(asyncio.create_task(url_logic(u, i+1, depth, destination)))
  
    await asyncio.gather(*tasks)


async def main():
    global COUNT
    if len(sys.argv) != 4:
        print("Wrong info passed")
        sys.exit(1)

    baseurl = sys.argv[1]
    destination = sys.argv[2]
    depth = int(sys.argv[3])

    await url_logic(baseurl, 0, depth, destination)

if __name__ == "__main__":
    asyncio.run(main())

