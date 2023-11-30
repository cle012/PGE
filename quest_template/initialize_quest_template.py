class QuestTemplateRepository:
    def __init__(self):
        self.templates = {}

    def add_template(self, quest_template):
        self.templates[quest_template.title] = quest_template

    def get_template(self, title):
        return self.templates.get(title)
