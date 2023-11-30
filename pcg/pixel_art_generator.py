from quest_template_repository import QuestTemplateRepository
from quest_generation import generate_quest

# Initialize the quest template repository
quest_repository = QuestTemplateRepository()

# Generate a quest based on a template
quest_template = quest_repository.get_template("Find the Lost Relic")
player_level = 4  # The player's level
new_quest = generate_quest(quest_template, player_level)
