"""Upstream source version fetcher for upheno-cross-species-ingest.

The upheno-cross-species.sssom.tsv mapping is tracked from the master
branch of obophenotype/upheno-dev.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from kozahub_metadata_schema import (
    now_iso,
    urls_from_download_yaml,
    version_from_github_branch,
)


INGEST_DIR = Path(__file__).resolve().parents[1]
DOWNLOAD_YAML = INGEST_DIR / "download.yaml"


def get_source_versions() -> list[dict[str, Any]]:
    ver, method = version_from_github_branch("obophenotype/upheno-dev", branch="master")
    return [
        {
            "id": "infores:upheno",
            "name": "uPheno Cross-Species Phenotype Mappings",
            "urls": urls_from_download_yaml(DOWNLOAD_YAML),
            "version": ver,
            "version_method": method,
            "retrieved_at": now_iso(),
        }
    ]
