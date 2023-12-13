from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Your NPC generation logic would go here, and you'd pass the results to the template
    npc = generate_npc()  # Replace with your actual function call
    return render_template('index.html', npc=npc)

def generate_npc():
    # Your NPC generation code here
    return {"name": "Generated NPC", "attributes": "NPC attributes"}

if __name__ == '__main__':
    app.run(debug=True)
