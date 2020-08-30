from util import read_content,find_links,write_content
import sys
import asyncio

URLList = []
COUNT = 0
loop = asyncio.get_event_loop()


async def url_logic(url,i,depth, destination):
    urls = []
    if i == depth:
        return
    if not url.startswith('http'):
        return

    ## 1. get the html page
    print(f"{url} step1")
    data = await read_content(url)

    ## 2. find out the links in the page and add it to a list
    print(f"{url} step2")
    find_links(data, urls) if depth > 0 else sys.exit(1)

    ## 3. write in the file (url,depth,content)
    global COUNT
    print(f"{url} step3")
    COUNT = write_content(url, str(depth), data, destination, COUNT)

    tasks = []
    print(f"Detected {len(urls)} urls in {url}")
    for u in urls:
        tasks.append(loop.create_task(url_logic(u, i+1, depth, destination)))
  
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
    loop.run_until_complete(main())

