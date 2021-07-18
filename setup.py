import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="ugents",
    version="1.0.1",
    author="Maehdakvan",
    author_email="visitanimation@google.com",
    description="UserAgents generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DedInc/ugents",
    project_urls={
        "Bug Tracker": "https://github.com/DedInc/ugents/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["ugents"],
    include_package_data = True,
    data_files   = [ ("ugents",  ["ugents/agents.json"])],
    python_requires=">=3.0",
)