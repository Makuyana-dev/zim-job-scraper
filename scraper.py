name: Auto Update Jobs

on:
  schedule:
    - cron: '0 */6 *'  # Runs every 6 hours
  workflow_dispatch:  # Lets you run it manually too

jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
        
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          
      - name: Install requirements
        run: pip install pandas
        
      - name: Run scraper
        run: python scraper.py
        
      - name: Commit and push if changed
        run: |
          git config --global user.name 'github-actions'
          git config --global user.email 'actions@github.com'
          git add jobs.csv
          git commit -m "Auto update jobs" || exit 0
          git push
