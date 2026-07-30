# Exercise: Comprehensions, Exceptions, and Dataclasses

project_names = ["Payments API", "Developer Portal", "Ops Console"]

# slugs = []
# for name in project_names:
#     slugs.append(name.lower().replace(" ", "-"))

slugs = [name.lower().replace(" ", "-") for name in project_names]

tasks = [
    {"title": "ship docs", "done": False},
    {"title": "cut release", "done": True},
    {"title": "announce launch", "done": False},
]

# open_titles = []
# for task in tasks:
#     if not task["done"]:
#         open_titles.append(task["title"])

open_titles = [task["title"] for task in tasks if not task["done"]]


def validate_project_name(name):
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Project name cannot be blank.")
    return cleaned


from dataclasses import dataclass


@dataclass
class Project:
    name: str
    slug: str
    archived: bool = False  # boolean with default value of False

    def archive(self) -> None:
        self.archived = True


if __name__ == "__main__":
    print(slugs)
    print(open_titles)

    try:
        validate_project_name(" ")
    except ValueError as e:
        print(f"Value error: {e}")

    test = Project(name="Test project", slug="test-project")
