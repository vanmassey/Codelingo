# Codelingo (`cdli`) 

A high-performance **Multilingual Code Reference Engine** built using Python and Pandas. `cdli` allows developers to instantly fetch optimized code snippets across multiple programming languages with explanations translated into their native human language.

## CLI Usage Syntax

```bash
# Fetch a snippet instantly: cdli get [programming_lang] [human_lang]
$ cdli get go es

# Check supported languages in the system matrix
$ cdli status
```

## Repository Structure

```text
codelingo/
├── .gitignore           # Keeps local cache files out of Git
├── LICENSE              # BSD 3-Clause + Senior Maintainer Exemption
├── README.md            # Project blueprint and documentation (This file)
└── backend/             # Python + Pandas engine and CLI logic
    ├── engine.py        # Core Pandas translation matrix
    └── cli.py           # Command-line interface logic
```

## Licensing

This project is licensed under the BSD 3-Clause License with a custom **Senior Maintainer (SM) Exemption** amendment. Commercial use of project or contributor names for marketing requires written authorization from an active Senior Maintainer.
