import asyncio
from playwright.async_api import async_playwright
import os
import time

async def verify_repel():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})

        # Open the local file
        file_path = os.path.abspath("main.html")
        await page.goto(f"file://{file_path}")

        # Wait for particles to load
        await page.wait_for_timeout(2000)

        # Take baseline screenshot (mouse at top-left)
        await page.mouse.move(0, 0)
        await page.wait_for_timeout(1000)
        await page.screenshot(path="/home/jules/verification/repel_baseline.png")

        # Move mouse to center
        center_x = 640
        center_y = 400
        await page.mouse.move(center_x, center_y)

        # Wait for repel effect
        await page.wait_for_timeout(1000)

        # Take screenshot with repel
        await page.screenshot(path="/home/jules/verification/repel_active.png")

        print("Screenshots taken: repel_baseline.png and repel_active.png")

        await browser.close()

if __name__ == "__main__":
    if not os.path.exists("/home/jules/verification"):
        os.makedirs("/home/jules/verification")
    asyncio.run(verify_repel())
