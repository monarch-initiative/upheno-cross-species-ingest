from pathlib import Path

import duckdb

nodes_file = "output/upheno_phenotype_to_phenotype_nodes.tsv"
edges_file = "output/upheno_phenotype_to_phenotype_edges.tsv"


# Nodes
if Path(nodes_file).exists():
    query = f"""
    SELECT category, split_part(id, ':', 1) as prefix, count(*)
    FROM '{nodes_file}'
    GROUP BY all
    ORDER BY all
    """
    duckdb.sql(f"copy ({query}) to 'output/upheno_phenotype_to_phenotype_nodes_report.tsv' (header, delimiter '\t')")

# Edges
if Path(edges_file).exists():
    query = f"""
    SELECT category, split_part(subject, ':', 1) as subject_prefix, predicate,
    split_part(object, ':', 1) as object_prefix, count(*)
    FROM '{edges_file}'
    GROUP BY all
    ORDER BY all
    """
    duckdb.sql(f"copy ({query}) to 'output/upheno_phenotype_to_phenotype_edges_report.tsv' (header, delimiter '\t')")

nodes_file = "output/upheno_phenotype_to_phenotype_filtered_nodes.tsv"
edges_file = "output/upheno_phenotype_to_phenotype_filtered_edges.tsv"


# Nodes
if Path(nodes_file).exists():
    query = f"""
    SELECT category, split_part(id, ':', 1) as prefix, count(*)
    FROM '{nodes_file}'
    GROUP BY all
    ORDER BY all
    """
    duckdb.sql(f"copy ({query}) to 'output/upheno_phenotype_to_phenotype_filtered_nodes_report.tsv' (header, delimiter '\t')")

# Edges
if Path(edges_file).exists():
    query = f"""
    SELECT category, split_part(subject, ':', 1) as subject_prefix, predicate,
    split_part(object, ':', 1) as object_prefix, count(*)
    FROM '{edges_file}'
    GROUP BY all
    ORDER BY all
    """
    duckdb.sql(f"copy ({query}) to 'output/upheno_phenotype_to_phenotype_filtered_edges_report.tsv' (header, delimiter '\t')")
