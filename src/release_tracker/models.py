# Like a data class, except we add that it's based on SQLModel, and that it corresponds to a table in the database
# class Book(SQLModel, table=True):  # Set defaults after the =
#     id: int | None = Field(
#         default=None, primary_key=True
#     )  # It would be None if a book isn't saved yet
#     title: str = Field(index=True)
#     author: str
#     pages: int | None = Field(default=None)


from datetime import UTC, datetime
from typing import Annotated

from pydantic import StringConstraints
from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel

# We use Annotated like we did before to define a string with some specific constraints / properties
ProjectName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=2),
]


class ProjectBase(SQLModel):  # common attributes for any project
    name: ProjectName = Field(  # using ProjectName here means that anytime a name gets saved, we strip whitespace (see above)
        unique=True
    )  # specify that the name needs to be unique in the database
    description: str | None = None


def utc_now() -> datetime:
    return datetime.now(UTC)


class Project(ProjectBase, table=True):
    __tablename__ = "projects"
    id: int | None = Field(default=None, primary_key=True)
    slug: str = Field(unique=True)
    created_at: datetime = Field(
        default_factory=utc_now,
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )


# We also need to create read and write schemas, which might look something like:
class ProjectCreate(ProjectBase):
    pass  # here we just inherit from ProjectBase, we don't need anything else


class ProjectUpdate(SQLModel):
    name: ProjectName | None = None
    description: str | None = None


class ProjectRead(ProjectBase):
    id: int
    slug: str
    created_at: datetime
