from datetime import datetime

from pymosaik import Node, Key, Field, ListField
from pymosaik.mosaik_types import FieldType


class Paper(Node):

    def __init__(self, Doi, PublishTime, Sha, Source, Title, License, Abstract, FullText, Authors, Journal, Pmcid, PubmedId, MicrosoftAcademicPaperID, WHOCovidence):
        self._MicrosoftAcademicPaperID = MicrosoftAcademicPaperID
        self._PubmedId = PubmedId
        self._Pmcid = Pmcid
        self._Journal = Journal
        self._Authors = Authors
        self._FullText = FullText
        self._Abstract = Abstract
        self._License = License
        self._Title = Title
        self._Source = Source
        self._Sha = Sha
        self._PublishTime = PublishTime
        self._Doi = Doi
        self._WHOCovidence = WHOCovidence

    @Key
    def Doi(self):
        return self._Doi

    @Field(FieldType.Time)
    def PublishTime(self):
        return self._PublishTime

    @Field(FieldType.String)
    def Sha(self):
        return self._Sha

    @Field(FieldType.String)
    def Source(self):
        return self._Source

    @Field(FieldType.String)
    def Title(self):
        return self._Title

    @Field(FieldType.String)
    def License(self):
        return self._License

    @Field(FieldType.String)
    def Abstract(self):
        return self._Abstract

    @Field(FieldType.String)
    def FullText(self):
        return self._FullText

    @Field(FieldType.String)
    def Authors(self):
        return self._Authors

    @Field(FieldType.String)
    def Journal(self):
        return self._Journal

    @Field(FieldType.String)
    def Pmcid(self):
        return self._Pmcid

    @Field(FieldType.String)
    def PubmedId(self):
        return self._PubmedId

    @Field(FieldType.String)
    def MicrosoftAcademicPaperID(self):
        return self._MicrosoftAcademicPaperID

    @Field(FieldType.String)
    def WHOCovidence(self):
        return self._WHOCovidence

    @staticmethod
    def from_csv_row(row, header):
        def parse_timestamp(timestring):
            if len(timestring) == 4:
                return datetime.fromisocalendar(int(timestring), 1, 1)
            else:
                try:
                    return datetime.fromisoformat(timestring)
                except:
                    return datetime.fromtimestamp(0)

        return Paper(Sha=row[header["sha"]],
                     Source=row[header["source_x"]],
                     Title=row[header["title"]],
                     Doi=row[header["doi"]],
                     Pmcid=row[header["pmcid"]],
                     PubmedId=row[header["pubmed_id"]],
                     License=row[header["license"]],
                     Abstract=row[header["abstract"]],
                     FullText=row[header["full_text_file"]],
                     PublishTime=parse_timestamp(row[header["publish_time"]]),
                     Authors=row[header["authors"]],
                     Journal=row[header["journal"]],
                     MicrosoftAcademicPaperID=row[header['Microsoft Academic Paper ID']],
                     WHOCovidence=row[header['WHO #Covidence']])


class Author(Node):

    def __init__(self, First, Middle, Last, Suffix, Email):
        self._Email = Email
        self._Suffix = Suffix
        self._Last = Last
        self._Middle = Middle
        self._First = First

    @Key
    def FullName(self):
        return " ".join([self.First()] + self.Middle() + [self.Last()])

    @Field(FieldType.String)
    def First(self):
        return self._First

    @ListField(FieldType.String)
    def Middle(self):
        return self._Middle

    @Field(FieldType.String)
    def Last(self):
        return self._Last

    @Field(FieldType.String)
    def Suffix(self):
        return self._Suffix

    @Field(FieldType.String)
    def Email(self):
        return self._Email


class Affiliation(Node):

    def __init__(self, Laboratory, Institution):
        self._Laboratory = Laboratory
        self._Institution = Institution

    @Key
    def FullName(self):
        return f"{self.Laboratory()}, {self.Institution()}".strip().strip(",")

    @Field(FieldType.String)
    def Laboratory(self):
        return self._Laboratory

    @Field(FieldType.String)
    def Institution(self):
        return self._Institution


class Location(Node):
    def __init__(self, Settlement, Country):
        self._Settlement = Settlement
        self._Country = Country

    @Key
    def FullName(self):
        return f"{self.Settlement()}, {self.Country()}".strip().strip(",")

    @Field(FieldType.String)
    def Settlement(self):
        return self._Settlement

    @Field(FieldType.String)
    def Country(self):
        return self._Country


class Journal(Node):
    def __init__(self, Name):
        self._Name = Name

    @Key
    def Name(self):
        return self._Name


class Disease(Node):

    def __init__(self, Id, Label, XRefs, Synonyms):
        self._Id = Id
        self._Label = Label
        self._XRefs = XRefs
        self._Synonyms = Synonyms

    @Key
    def Id(self):
        return self._Id

    @Field(FieldType.String)
    def Label(self):
        return self._Label

    @ListField(FieldType.String)
    def XRefs(self):
        return self._XRefs

    @ListField(FieldType.String)
    def Synonyms(self):
        return self._Synonyms
