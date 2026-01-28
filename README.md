# upheno-cross-species-ingest

An automated ingest transforming the uPheno data artifact upheno-cross-species.sssom.tsv into KGX format.

## Requirements

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just) (optional, for task running)

## Installation

```bash
uv sync --group dev
```

## Usage

To see available commands:

```bash
just
```

### Download and Transform

Download the source data:

```bash
just download
```

Run all transforms:

```bash
just transform-all
```

Or run the full pipeline (download + transform):

```bash
just run
```

### Testing

```bash
just test
```

### Linting and Formatting

```bash
just lint
just format
```

## Data Source

This ingest transforms the uPheno cross-species SSSOM mapping file, which contains phenotype mappings across different species from the Unified Phenotype Ontology (uPheno) project.

### Source Files

- `upheno-cross-species.sssom.tsv` - Cross-species phenotype mappings from the uPheno project

### Nodes and Edges

- **PhenotypicFeature nodes** - Phenotype entities from various species ontologies (HP, MP, ZP, etc.)
- **Association edges** - `homologous_to` relationships between phenotypes from different species

## Project Structure

- `download.yaml` - Configuration for downloading source data
- `src/transform.yaml` - Koza transform configuration
- `src/transform.py` - Transform code
- `tests/` - Unit tests
- `output/` - Generated KGX files (gitignored)
- `data/` - Downloaded source data (gitignored)

## GitHub Actions

- `test.yaml` - Run tests on push and PR
- `create-release.yaml` - Create releases
- `deploy-docs.yaml` - Deploy documentation to GitHub Pages
- `update-docs.yaml` - Update documentation after releases
