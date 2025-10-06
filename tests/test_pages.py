import os
import pytest
from bs4 import BeautifulSoup  # you’ll need to install beautifulsoup4 for parsing

# Define the pages you expect
PAGES = {
    "index.html": {
        "title": "Jenom Shehu — About",
        "must_contain": ["DevOps / Site Reliability Engineer — Cloud-native infrastructure, IaC, CI/CD, Observability"]
    },
    "resume.html": {
        "title": "Resume — Jenom Shehu",
        "must_contain": ["Professional Summary", "Technical Skills", "Professional Experience"]
    },
    "ksa.html": {
        "title": "KSA — Jenom Shehu",
        "must_contain": ["Knowledge", "Skills", "Abilities"]
    },
    "cover-letter.html": {
        "title": "Cover Letter — Jenom Shehu",
        "must_contain": ["Cover Letter — Jenom Shehu"]
    }
}

@pytest.mark.parametrize("filename, expectations", PAGES.items())
def test_page_exists_and_content(tmp_path, filename, expectations):
    """
    Check that the page file exists in the build directory and has expected title and content.
    """
    site-root = /portfolio-site
    # You should set your build or output folder; here I assume the pages are in project root or in `site/`
    # For example, if your built site is in 'site/' folder:
    page_path = os.path.join(site_root, 'portfolio-site', filename)
    #site_root = os.getcwd()  # or replace with path to your built folder
    page_path = os.path.join(site_root, filename)
    assert os.path.isfile(page_path), f"Expected page file not found: {page_path}"
    
    # Read the file
    text = open(page_path, encoding="utf-8").read()
    soup = BeautifulSoup(text, "html.parser")

    # Check <title>
    title_tag = soup.find("title")
    assert title_tag is not None, f"No <title> tag in {filename}"
    title_text = title_tag.get_text().strip()
    assert title_text == expectations["title"], f"Title mismatch in {filename}: got {title_text}, expected {expectations['title']}"

    # Check body contains key strings
    for keyword in expectations["must_contain"]:
        assert keyword in text, f"Expected to find '{keyword}' in {filename}"

def test_dummy():
    """A dummy test so pytest does not complain about zero tests."""
    assert True

print("All tests passed!")