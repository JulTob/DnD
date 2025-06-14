# /app/__init__.py
from Minion import gennie, setup_logging, Initialized, Alert, Inform, Warning

# Create a spinner instance.
gennie.update(message="Inquiring Knowledge Atlas!", cycle=['🧭','🗺️'])

gennie.update("Flask alchemy reacting!", ["🥚","🐣","🐦‍🔥","🔥"],"Red" )
from flask import Flask

gennie.update("Secrets unraveled!",["🔎","🔍"])
import secrets

gennie.update("Time Mastered!",["⌛️","⏳"])
from datetime import timedelta

gennie.update("Routes constructed!",["🚦","🚥"])
from app.routes import init_routes


gennie.update("All Initial atlases procured.", ['🔅', '🔆'])


setup_logging()

def create_app():
	Initialized("Application summoned!")
	gennie.update("Creating App", ["💀","☠️"])

	# Create Flask app
	app = Flask(__name__)
	Initialized("Flask app object created.")

	# Configure security and sessions
	app.secret_key = secrets.token_urlsafe(16)
	Inform(f"Secret key set: {app.secret_key[:4]}... (hidden for security)")
	app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=8)
	Inform("Session lifetime configured: 8 days.")

	# Initialize routes
	try:
		init_routes(app)
		Inform(f"Routes aboard: {len(app.url_map._rules)} total!")
	except Exception as e:
		Alert("Failed to initialize routes.", error=e)

	# Error Handler (Optional?)
	@app.errorhandler(404)
	def not_found(e):
		from flask import render_template
		#return "<h1>The requested scroll was not found!</h1> <h2>These are uncharted waters, Adventurer!</h2>", 404
		Alert("404 - Not found\n", e)
		return render_template(
				"404.html",
				title="404 - 📜 Summoning Scroll Not Found"
				), 404

	# Global Error Handler (Optional?)
	@app.errorhandler(Exception)
	def handle_exception(e):
		from flask import render_template
		Alert("🏹 Handler Call: An Unhandled Exception scaped from the Dungeon! Summoning the Internal Server Error(500) hunter!!!", error=e)
		return render_template(
				"500.html",
				title="500 - 📜 Summoning Scroll Not Found"
				), 500

	Inform("Flask app successfully created and configured.")
	return app
