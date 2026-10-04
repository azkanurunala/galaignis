import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        html="<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'></head><body>"+open('kalender-tayang.html').read()+"</body></html>"
        open('/tmp/claude-0/k.html','w').write(html)
        pg=await b.new_page(viewport={'width':1280,'height':1100})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///tmp/claude-0/k.html'); await pg.wait_for_timeout(800)
        await pg.click('#nextM'); await pg.wait_for_timeout(200)
        await pg.screenshot(path='k1.png',full_page=True)
        await pg.click('[data-id="e001-full"]'); await pg.wait_for_timeout(300)
        await pg.screenshot(path='k2.png')
        m=await b.new_page(viewport={'width':400,'height':860})
        await m.goto('file:///tmp/claude-0/k.html'); await m.wait_for_timeout(500)
        await m.click('#vAgenda'); await m.wait_for_timeout(200)
        await m.screenshot(path='k3.png')
        print('errors',errs)
        await b.close()
asyncio.run(main())
