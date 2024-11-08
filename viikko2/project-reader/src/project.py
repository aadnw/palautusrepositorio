class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _list_dependencies(self, dependencies):
        if len(dependencies) > 0:
            list = ""
            for depency in dependencies:
                list += "- " + depency + "\n"
            return list
        else:
            return "-"

    def _list_authors_(self, authors):
        list = ""
        for author in authors:
            list += "- " + author + "\n"
        return list

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n{self._list_authors_(self.authors)}"
            f"\nDependencies:\n{self._list_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies:\n{self._list_dependencies(self.dev_dependencies)}"
        )
