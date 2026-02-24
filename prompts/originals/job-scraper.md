# Pune Jobs Scraper Prompt

**Score**: 9.2/10
**Tokens**: ~300
**Use Case**: Creating a robust, anti-bot-bypassing web scraper for job portals in Pune.

## The Prompt

```text
Build a Python web scraper using Playwright and BeautifulSoup4 to extract job listings for "Software Engineer" in Pune, Maharashtra.

**REQUIREMENTS**:
1. **Target**: popular job boards (simulated logic if specific ones are blocked).
2. **Data extraction**: Job Title, Company, Location (must strictly be Pune or remote), Salary (if visible), and Tech Stack keywords.
3. **Anti-bot**: Implement random delays (2-5s), user-agent rotation, and stealth mode.
4. **Output**: Save results into a `pune_jobs.csv` using the `csv` module, and append to a SQLite database.
5. **Resilience**: Handle timeouts gracefully. If a selector fails, log the error and skip to the next listing instead of crashing.
```
