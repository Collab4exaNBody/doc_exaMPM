# exaMPM documentation

Sources of the [exaMPM](https://github.com/Collab4exaNBody/exaMPM) online documentation, built with
[Zensical](https://zensical.org/) (same setup as [doc_exaStamp](https://github.com/Collab4exaNBody/doc_exaStamp)).

## Prerequisites

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Preview as you write

```bash
zensical serve
```

Open [localhost:8000](http://localhost:8000): the site is rebuilt when a source file changes.

## Build the site

```bash
zensical build --clean
```

The static site is written to `site/`. On every push to `main`, `.github/workflows/build-and-deploy.yml` builds it
and deploys it to GitHub Pages.

## Configuration files and example decks

`docs/files/` holds copies of exaMPM's `data/config/*.msp` and `example/<name>/<name>.msp`, included in the pages
with `--8<-- "docs/files/<file>"`, and `docs/images/examples/` the example pictures `example/<name>/<name>.png`.
After a change in exaMPM, refresh them with:

```bash
scripts/sync_files.sh /path/to/exaMPM
```

The pictures are rendered with `pvbatch scripts/render_example.py` (see the page *User Guide > Outputs >
Visualization*).
