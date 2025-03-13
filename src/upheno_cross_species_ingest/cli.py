"""Command line interface for upheno cross species ingest."""
import logging

from pathlib import Path

from kghub_downloader.download_utils import download_from_yaml
from kghub_downloader.model import DownloadOptions

from koza.cli_utils import transform_source
import typer

app = typer.Typer()
logger = logging.getLogger(__name__)


@app.callback()
def callback(version: bool = typer.Option(False, "--version", is_eager=True),
):
    """upheno cross species ingest CLI."""
    if version:
        from upheno_cross_species_ingest import __version__
        typer.echo(f"upheno cross species ingest version: {__version__}")
        raise typer.Exit()


@app.command()
def download(force: bool = typer.Option(False, help="Force download of data, even if it exists")):
    """Download data for upheno cross species ingest."""
    typer.echo("Downloading data for upheno cross species ingest...")
    download_config = Path(__file__).parent / "download.yaml"
    download_options = DownloadOptions()
    download_options.ignore_cache = True 
    download_from_yaml(yaml_file=download_config, output_dir=".", download_options=download_options)


@app.command()
def transform(
    output_dir: str = typer.Option("output", help="Output directory for transformed data"),
    row_limit: int = typer.Option(None, help="Number of rows to process"),
    verbose: int = typer.Option(False, help="Whether to be verbose"),
):
    """Run the Koza transform for upheno cross species ingest."""
    typer.echo("Transforming data for upheno cross species ingest...")
    #transform_code = Path(__file__).parent / "transform.yaml"
    transform_code = Path(__file__).parent / "transform.yaml"
    transform_source(
        source=transform_code,
        output_dir=output_dir,
        output_format="tsv",
        row_limit=row_limit,
        verbose=verbose,
    )
    
@app.command()
def transform_filtered(
    output_dir: str = typer.Option("output", help="Output directory for transformed data"),
    row_limit: int = typer.Option(None, help="Number of rows to process"),
    verbose: int = typer.Option(False, help="Whether to be verbose"),
):
    """Run the Koza transform for upheno cross species ingest."""
    typer.echo("Transforming data for upheno cross species ingest...")
#    transform_code = Path(__file__).parent / "transform_filtered.yaml"
    transform_code = Path(__file__).parent / "transform_filtered.yaml"
    transform_source(
        source=transform_code,
        output_dir=output_dir,
        output_format="tsv",
        row_limit=row_limit,
        verbose=verbose,
    )

if __name__ == "__main__":
    print("HEY")
    app()
