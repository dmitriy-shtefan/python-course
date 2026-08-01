class Project:
    def __init__(self, title, technologies):
        self.title = title
        self.technologies = technologies

    def add_technology(self, technology):
        self.technologies.add(technology)

    def technology_count(self):
        return len(self.technologies)


project = Project("Контакти", {"Python", "Streamlit", "Python"})

project.add_technology("Git")

print(sorted(project.technologies))     # Git, Python, Streamlit
print(project.technology_count())       # 3
