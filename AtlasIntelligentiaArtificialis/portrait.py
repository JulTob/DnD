# AtlasArcana/portrait.py


def generate_npc_portrait(prompt, api_key):
	import requests
	headers = {
		"Authorization": f"Bearer {api_key}"
	}
	data = {
		"model":"dall-e-3",
		"size": "350x350",
		"quality": "hd",
		"prompt": prompt,
		"n": 1  # Number of images to generate
	}
	try:
		response = requests.post("https://api.openai.com/v1/images/generations", headers=headers, json=data)
		if response.status_code == 200:
			return response.json()['data'][0]['url']  # URL of the generated image
		else:
			print("Error generating portrait:", response.status_code, response.text)
			return None
	except Exception as e:
		print("Exception in generate_npc_portrait:", str(e))
		return None



def new_dalle_prompt(npc_data: dict) -> str:
	"""
    Generate a DALL-E prompt based on NPC data.
    Preconditions:
    - 	<npc_data> is a dictionary with expected keys:
	*		'gender',
	* 		'subrace',
	*		'background',
	*		'name',
	*		'title',
	*		'alignment',
	*		'race'.

    Postconditions:
    - Returns a descriptive string to be used as a prompt.
    """

	if npc_data['gender'] == "he":
		gender = "male"
	elif npc_data['gender']== "she":
		gender = "female"
	else:
		gender = "androginous"

	description = f'''
	Create a masterful, detailed and artistic ink sketch portrait of a {npc_data['subrace']} {npc_data['background']} with {gender} gender, known as {npc_data['name']}, {npc_data['title']}.
	The minimalistic sketch should emphasize fantastic elements, and highly detailed facial features, capturing the essence of a {npc_data['alignment']} personality and unique {npc_data['race']} traits.
	Focus on the character's face and expression.The style should be hyperrealistic, with gothicpunk and steampunk aesthetics, in the style of high fantasy art.
	The artwork should be reminiscent of an arcane grimoire, such as in a bestiary of high fantasy or a necronomicon with arcane symbols.
	No text.
	'''
	'''
	The style should mirror artists such as Muja, DaVinci, Caravaggio, Sorolla, Rembrandt, Goya, Monet, van Gogh, Klimt
	And should be inspired by the great artistic movements of Art Nouveau, High Renaissance, Romaticism, 90's comics, 2000's street art, hyperrealistic techniques, digital art aesthetics, cyberpunk, neopunk, solarpunk, punk motifs,
	'''
	return description
