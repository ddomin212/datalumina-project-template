# Data Project Template

## Cookiecutter Data Science
This project template is a simplified version of the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org) template, created to suit the needs of Edima.

## Adjusting .gitignore
Ensure you adjust the `.gitignore` file according to your project needs. For example, since this is a template, the `/data/` folder is commented out and data will not be exlucded from source control:

```plaintext
# exclude data from source control by default
# /data/
```

Typically, you want to exclude this folder if it contains either sensitive data that you do not want to add to version control or large files.

## Duplicating the .env File
To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.

## Creating a library
Complete this part of the `pyproject.toml` file with your own information.
```toml
[tool.poetry]
name = "edmund-lib" # name of the library, should be something like
                    # edmund-parsers-eplan, edmund-ai-eval etc., template being edmund-{related topic}-{name}
                    # you also have to rename the folder with the same name, but replace - with _

version = "0.1.1" # change this via make version v=<the version upgrade> command, follows semantic versioning (major.minor.patch)
                  # i.e. so if you want to change the major version, you do make version v=major. This is mainly for the main branch and
                  # integration with our friendos at the backend side :]

description = "very smart description"

authors = ["Generic Author <a@b.com>"] # author

readme = "README.md"
```
Then commit to git of `EDIMA-solutions`. Backend will install it via `poetry add https://<your username>:<your password>@github.com/EDIMA-solutions/<repo_name>.git`. It is very much recommended to have a `dev` and `main` brach, where `main` is what is actually in production, `dev` is just for your own experimenting.

## Project Organization

```
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
    └── download.py      <- downloads relevant data for repo
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the, and a short `-` delimited description, e.g.
│                         `1.0-initial-data-exploration`
│
├── examples            <- code examples
│
├── docs                <- documentation material except README (human, AI or code generated)
│
├── prompts             <- AI related
│     ├── few-shot-examples.py      <- examples for prompts
│     ├── prompts.py                <- actual prompts for the model
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── tests              <- tests for the library based on data in ./data
│     ├── __init__.py
│     ├── test.py
│
└── edmund-lib            <- Source code for the following library which will be used on the backend, **please rename, also in `pyproject.toml`**
```