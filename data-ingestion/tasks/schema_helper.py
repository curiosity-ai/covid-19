from pymosaik import Mosaik
from pymosaik.mosaik_types import SchemaCreationMode
from schemas.edges import *
from schemas.nodes import *


def create_graph_schema(msk: Mosaik):
    msk.schemas.exists(HasAffiliation.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(AffiliatedTo.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(LocatedIn.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(HasInstitution.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(BasedOn.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(HasAuthor.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(AuthorOf.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(PublishedIn.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(HasPaper.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(MentionsDisease.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(DiseaseAppearsIn.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(MentionsGene.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(GeneAppearsIn.schema(), SchemaCreationMode.CreateOnly)

    msk.schemas.exists(Paper.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(Author.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(Affiliation.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(Location.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(Journal.schema(), SchemaCreationMode.CreateOnly)
    msk.schemas.exists(Disease.schema(), SchemaCreationMode.CreateOnly)
