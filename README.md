# DuckAPI

There will be a blog post, I'll put the link here if I remember

## Getting started

The repository can be found here [github.com/Nintorac/duckapi](https://github.com/Nintorac/duckapi)


First edit the `.env` file so that `PROJECT_ROOT` var is pointing to the root of this repository.

Then, assuming you already have conda installed,

```bash
conda create -n duckapi python=3.10 -y
conda activate duckapi
pip install poetry
make install_dev
make test
```
