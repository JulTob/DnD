# app.py
print("App started")
from Minion import gennie, Initialized

gennie.start()
gennie.update(
	"Summoning Generations of Heroes and Villains",
	[".","..","..."])


gennie.update(
	"App Creation! 🏗️",
	["⛺️","🛖 ","🏚️ ","🏠 ","🏛 ️","🏯 ","🏰 "])
from app import create_app

gennie.update(
	"Flask alchemy reacting! ⚗️",
	["🌕","🌖","🌗","🌘","🌑","🌒","🌓","🌔"],
	"green")
from flask import Flask

gennie.update(
	"App Rising",
	["🏔️","⛰️","🌋","⛰️"])
app = create_app()

gennie.update(
	"App Ready",
	["🎩","🐇"])
gennie.stop()

if __name__ == '__main__':
	# Create the application instance
	print("📳 App Runner Called")
	Initialized("⚓ Flask app about to set sail!")
	app.run(debug= True)
		# Use debug mode for development
		# Turn False for deployment
