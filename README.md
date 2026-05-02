# uPheno Cross-Species Phenotype Mappings

The [Unified Phenotype Ontology (uPheno)](https://github.com/obophenotype/upheno) provides cross-species phenotype mappings, enabling comparison of phenotypic data across different model organisms. This ingest transforms the uPheno cross-species SSSOM (Simple Standard for Sharing Ontological Mappings) file into phenotype-to-phenotype associations.

Data is downloaded from the uPheno project: `upheno-cross-species.sssom.tsv`

## Phenotype Associations

Each row in the SSSOM file represents a mapping between two phenotype terms from different species-specific ontologies (e.g. HP, MP, ZP, WBPhenotype). The ingest creates PhenotypicFeature nodes for both subject and object phenotypes, connected by a `homologous_to` association.

Mapping metadata (justification, subject source, object source) from the SSSOM file is preserved as attributes on the association.

**Biolink Captured:**

- `biolink:PhenotypicFeature` (nodes)
    - id (phenotype term ID)
    - name (phenotype label)

- `biolink:Association`
    - id (generated)
    - subject (phenotype term ID)
    - predicate (`biolink:homologous_to`)
    - original_predicate (predicate ID from SSSOM row)
    - object (phenotype term ID)
    - subject_category (`biolink:PhenotypicFeature`)
    - object_category (`biolink:PhenotypicFeature`)
    - has_attribute (mapping justification, subject source, object source)
    - primary_knowledge_source (`infores:upheno`)
    - knowledge_level (`prediction`)
    - agent_type (`data_analysis_pipeline`)

## Citation

Matentzoglu N, Bello SM, Stefancsik R, Alghamdi SM, Anagnostopoulos AV, Balhoff JP, Balk MA, Bradford YM, Bridges Y, Callahan TJ, Caufield H, Cuzick A, Carmody LC, Caron AR, de Souza V, Engel SR, Fey P, Fisher M, Gehrke S, Grove C, Hansen P, Harris NL, Harris MA, Harris L, Ibrahim A, Jacobsen JOB, Kohler S, McMurry JA, Munoz-Fuentes V, Munoz-Torres MC, Parkinson H, Pendlington ZM, Pilgrim C, Robb SM, Robinson PN, Seager J, Segerdell E, Smedley D, Sollis E, Toro S, Vasilevsky N, Wood V, Haendel MA, Mungall CJ, McLaughlin JA, Osumi-Sutherland D. The Unified Phenotype Ontology (uPheno): A framework for cross-species integrative phenomics. Genetics. 2025;229(3):iyaf027. doi: 10.1093/genetics/iyaf027. PMID: 40048704

## License

BSD-3-Clause
