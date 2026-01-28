# upheno-cross-species-ingest

This is a Koza ingest repository for transforming uPheno cross-species phenotype mappings into Biolink model format.

## Project Structure

- `download.yaml` - Configuration for downloading uPheno SSSOM data
- `src/` - Transform code and configuration
  - `transform.py` / `transform.yaml` - Main transform for phenotype-to-phenotype associations
- `tests/` - Unit tests for transforms
- `output/` - Generated nodes and edges (gitignored)
- `data/` - Downloaded source data (gitignored)

## Key Commands

- `just run` - Full pipeline (download -> transform)
- `just download` - Download uPheno SSSOM data
- `just transform-all` - Run all transforms
- `just test` - Run tests

## Data Source

This ingest transforms upheno-cross-species.sssom.tsv which contains cross-species phenotype mappings from the uPheno project. The transform creates PhenotypicFeature nodes and homologous_to associations between phenotypes from different species.
