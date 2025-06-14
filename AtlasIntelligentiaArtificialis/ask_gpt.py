# AtlasArcana/openai_integration.py

import openai

def ask_chatgpt(question: str, api_key: str) -> str:
    """
    Use OpenAI's Completion API to answer a question.
    Preconditions:
    - question is a non-empty string.
    - api_key is a valid OpenAI API key.

    Postconditions:
    - Returns the response from OpenAI as a string.
    """
    assert isinstance(question, str) and question.strip(), "Precondition failed: question must be a non-empty string."
    assert isinstance(api_key, str) and api_key.strip(), "Precondition failed: api_key must be a valid string."

    try:
        openai.api_key = api_key

		# Use the Completion API to ask the question
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
				## 	You can specify other models as well:
				#		"text-davinci-002",
				#		"curie",
				#		"ada"
            prompt=question,
            max_tokens=1000,
				# Limit the response length, adjust as needed
            temperature=1
        )
        result = response.choices[0].text.strip()
        assert isinstance(result, str), "Postcondition failed: result must be a string."
        return result
    except Exception as e:
        return f"Error: {e}"


def ask_chatgpt2(question):
    try:
        import openai

        # Open AI Key
        keyFile = open("key.txt", "r")
        key = keyFile.read()
        openai.api_key = key
        keyFile.close()

        # Use the Completion API to ask the question
        response = openai.Completion.create(
            model = "gpt-3.5-turbo-instruct", #"text-davinci-002", ## You can specify other models as well: "text-davinci-002", "curie", "ada
            prompt=question,
            max_tokens=500,  # Limit the response length, adjust as needed
            temperature=1
        )
        return response.choices[0].text.strip()
    except:
        return ""


'''






    result += "\n" + r



    result += "\n" + "\n꧁  Their Story ꧂\n\n"
    s = ""
    s += "\n"
    s += " - Traits -"
    s += "\n"
    s += npc.trait
    s += " - Ideal -"
    s += "\n"
    s += npc.ideal
    s += "\n"
    s += " - Story Hook -"
    s += "\n"
    ph = npc.plothook
    s += ph


    try:
        question = "Craft the presentation for a D&D NPC: "
        question += "\n Name: " + npc.name
        question += "\n Known as: " + npc.title
        question += "\n Race " + npc.race + "\n Subrace:" + npc.subrace
        question += "\n Alignment: " + npc.alignment
        question += "\n Background:" + npc.archetype
        question += "\n Traits:" + npc.trait
        question += "\n Ideals:" + npc.ideal
        question += "\n Problem or Plot Hook: " + ph
        question += "\n Suggest a creative problem that leads to a conflict for the group. "
        question += "This conflict must be specific and well defined, having a certain success state and fail state."
        question += "The problem must be solvable in at least three different ways: One social, one using skills, and one martial. "
        question += "\n The group of players should be able to adopt a possition of antagonists or allies with the NPC."
        question += "\n Expand details as necessary. "
        question += "\n Write it in the style of " + Style()
        question += "\n Write it in first person, as if he was introducing himself, and use three paragraphs of about 150 words each, expanding where appropiate. "
        question += "\n The first paragraph must be a presentation containing information of their name and background. "
        question += "\n The second paragraph must expand on their ideals and goals."
        question += "\n The third paragraph must explain why the player's characters may help or confront the NPC, using the Ploot Hook as the source of the conflict."
        answer = ask_chatgpt(question)
        result += "\n" + answer
        result += "\n" + s
    except Exception as e:
2        result += "\n" + s
        result += "\n" + f"Encountered an error: {e}"

    return result

print(NPC_gen())

'''
