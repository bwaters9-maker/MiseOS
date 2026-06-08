
import asyncio
from playwright.async_api import async_playwright
import os
import time

async def benchmark():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        file_path = os.path.abspath("miseos_dashboard.html")
        await page.goto(f"file://{file_path}")

        # Create a large recipe
        large_recipe = "\n".join([f"1 lb veal" for _ in range(400)])

        # Inject the recipe and measure time
        # We use JSON.stringify to safely pass the string
        start_time = time.time()
        await page.evaluate("""(recipe) => {
            const editor = document.getElementById('recipeEditor');
            editor.value = recipe;
            calculateRecipeCost();
        }""", large_recipe)
        end_time = time.time()

        execution_time = (end_time - start_time) * 1000
        print(f"Baseline Execution Time for 400 lines: {execution_time:.2f} ms")

        # Also measure formatMarkdownText
        long_text = "**Bold** *Italic* `code` \n" * 100
        start_time = time.time()
        await page.evaluate("""(text) => {
            formatMarkdownText(text);
        }""", long_text)
        end_time = time.time()

        format_time = (end_time - start_time) * 1000
        print(f"Baseline formatMarkdownText Time for 400 lines: {format_time:.2f} ms")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(benchmark())
