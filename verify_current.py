
import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local HTML file
        file_path = os.path.abspath("miseos_dashboard.html")
        await page.goto(f"file://{file_path}")

        # Check for errors in console
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(err.message))

        await page.wait_for_timeout(1000)

        print("Console Errors:", errors)

        # Check if the "Raw Total Cost" is calculated (it should be for the demo recipe)
        raw_total_cost = await page.inner_text("#rawTotalCost")
        print("Raw Total Cost:", raw_total_cost)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
