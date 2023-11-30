from quest_template_repository import QuestTemplateRepository

def generate_quest(template, player_level):
    quest = Quest(
        title=template.title,
        description=template.description,
        objectives=template.objectives,
        rewards=template.rewards,
        conditions=template.conditions,
        player_level=player_level
    )
    return quest
