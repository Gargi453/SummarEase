import setuptools

with open ("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "SSummarEase"
AUTHOR_USER_NAME = "Gargi453"
SRC_REPO = "textsummarization"
AUTHOR_EMAIL = "mahajangargi3@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP app",
    Long_description = long_description,
    Long_description_content = "Text/markdown",
    url = f"",
    project_url = {
        "Bug Tracker": f""
    },
    package_dir = {"":"src"},
    package = setuptools.find_packages(where = "src")
)
