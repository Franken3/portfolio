import json

from texts import Texts


class Mess:
	def __init__(self, prev_state, text_state):
		"""Constructor"""
		self.prev_state = prev_state
		self.text_state = text_state

	def to_JSON(self):
		return json.dumps(self, default = lambda o: o.__dict__, sort_keys = True, indent = 4)


states = {
	"start_state_message":        Mess('start_state_message', Texts.start_state_text),
	"bio_state_message":          Mess('start_state_message', Texts.bio_state_text),
	"about_state_message":        Mess('start_state_message', Texts.about_project_text),
	"all_projects_state_message": Mess('start_state_message', Texts.all_projects_text),
}

for i in range(len(Texts.projects_button_text)):
	states = states | {f'{Texts.projects_button_text[i]}': Mess("all_projects_state_message",
																Texts.projects_description_texts[i])}

