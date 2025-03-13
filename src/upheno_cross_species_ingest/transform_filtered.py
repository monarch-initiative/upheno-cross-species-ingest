import uuid  # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import *  # Replace * with any necessary data classes from the Biolink Model
from koza.cli_utils import get_koza_app

koza_app = get_koza_app("upheno_phenotype_to_phenotype_filtered")

while (row := koza_app.get_row()) is not None:
    #if(row['subject_source']=="obo:upheno" or row['object_source']=="obo:upheno"):
    #    continue
    
    subject_phenotype_entity = PhenotypicFeature(
        id=row["subject_id"],
        name=row["subject_label"],
        category=["biolink:PhenotypicFeature"],
    )
    object_phenotype_entity = PhenotypicFeature(
        id=row["object_id"],
        name=row["object_label"],
        category=["biolink:PhenotypicFeature"],
    )
    association = Association(
        id=str(uuid.uuid1()),
        subject=subject_phenotype_entity.id,
        original_subject="TEST",
        predicate="biolink:homologous_to",
        original_predicate=row["predicate_id"],
        object=object_phenotype_entity.id,
        subject_category="biolink:PhenotypicFeature",
        object_category="biolink:PhenotypicFeature",
        category=["biolink:Association"],
        primary_knowledge_source="infores:upheno",
        knowledge_source="upheno-cross-species.sssom.tsv",
        has_attribute=[f'"mapping_justification":"{row["mapping_justification"]}"',f'"subject_source":"{row["subject_source"]}"',f'"object_source":"{row["object_source"]}"'],
        knowledge_level=KnowledgeLevelEnum.prediction,
        agent_type=AgentTypeEnum.data_analysis_pipeline ,
    )
    koza_app.write(subject_phenotype_entity, object_phenotype_entity, association)
