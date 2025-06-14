# Minion.py
#import     logging
import     inspect
import     os
from     datetime import datetime

# Spinner
import traceback
import sys
import time
import threading
import itertools

class Spinner:
	def __init__(self, message="Loading", cycle=None, interval=2, color="cyan"):
		self.message = message
		self.cycle = cycle if cycle is not None else ["🌕","🌖","🌗","🌘","🌑","🌒","🌓","🌔"]
		self.interval = interval
		self.color = color
		self._counter = 120
		self._running = False
		self._lock = threading.Lock()
		self._thread = None

	def _spinner_task(self):
		while self._counter>0:
			for char in self.cycle:
				with self._lock:
					current_message = self.message
					current_color = self.color
				if self._counter<0:
					break
				sys.stdout.write("\r\033[K")
				sys.stdout.write(Color(f"\r🧞{current_message} {char}\t\t", self.color))
				sys.stdout.flush()
				time.sleep(self.interval)
				self._counter -= 1
		# Move on the line after stopping.
		sys.stdout.write(Color(f"\r🧞\t{current_message} {char}\t\n", self.color))

	def start(self, message="", cycle=["🔅","🔆"],color="blue"):
		self._running = True
		self._counter = 120
		self._thread = threading.Thread(target=self._spinner_task)
		self._thread.start()
		self.update(message,cycle,color)

	def update(self, message="", cycle = ["🌕","🌖","🌗","🌘","🌑","🌒","🌓","🌔"], color="cyan"):
		if not self._running:
			self.start()
		with self._lock:
			sys.stdout.write("\n")
			self.message = message
			self.cycle = cycle
			self.color = color
			self._counter = 120

	def update_message(self, new_message):
		with self._lock:
			self.message = new_message

	def update_cycle(self, new_cycle = ["🌕","🌖","🌗","🌘","🌑","🌒","🌓","🌔"]):
		with self._lock:
			self.cycle = new_cycle

	def update_color(self, new_color):
		with self._lock:
			self.color = new_color

	def stop(self):
		self._counter = -1
		if self._thread:
			self._thread.join()

# Global spinner that can be used across the app
gennie = Spinner("📯 Your Wish is our commands!",[""])

def Color(message="", color= "Black"):
	if color == "Black":
		return f"\033[1;90m{message}\033[0m"
	if color == "black":
		return f"\033[90m{message}\033[0m"
	if color == "Red":
		return f"\033[1;91m{message}\033[0m"
	if color == "red":
		return f"\033[91m{message}\033[0m"
	if color == "Green":
		return f"\033[1;92m{message}\033[0m"
	if color == "green":
		return f"\033[92m{message}\033[0m"
	if color == "Yellow":
		return f"\033[1;93m{message}\033[0m"
	if color == "yellow":
		return f"\033[93m{message}\033[0m"
	if color == "Blue":
		return f"\033[1;94m{message}\033[0m"
	if color == "blue":
		return f"\033[94m{message}\033[0m"
	if color == "Magenta":
		return f"\033[1;95m{message}\033[0m"
	if color == "magenta":
		return f"\033[95m{message}\033[0m"
	if color == "Cyan":
		return f"\033[1;96m{message}\033[0m"
	if color == "cyan":
		return f"\033[96m{message}\033[0m"
	return Color(message,"Black")

def Bold(message=""):
	return f"\033[1m{message}\033[22m"


main_minion = Color("🧞‍♂️:\t Dark Lord! A Minion arrived with a message!", "Black") # Genie = All powerful
alert_minion = "🔴 🧜🏽‍♀️: ALERT‼️‼️" # Siren = Alert
messenger_minion = f"⚪️ 🕊️: I have a message:" # Message Pidgeon
data_retrieval_minion ="🟣 🕸️🕷️🕸️: I catched thisss:" # Spider (Web), catches bugs and data
warning_minion = f"🟠 🧌: Theres danger ahead:" # Troll: Warden of the way
news_minion = f"🌕 🐦‍🔥: A new summon began:" # Fenix: Starts anew every day
ends_minion = f"🌑 🦉: A summon ended:" # Owl: Comes out at the end of the day
fail_minion = f"🟤 🧟: A summon failed:" # Zombie: It died
record_minion = f"🟢 🐲: Conquest Log:" # Ancient Dragon: Remembers


# Automatically configure logging when the module is imported
def setup_logging():

	gennie.start("🧞‍ Minions Ready...")

def Log(message=""):
	return_message = main_minion
	return_message += '\n'
	return_message += message
	print(return_message)

def get_call_tree(start_files=None,stop_files=None, stop_functions= None):
	"""
	Builds a visually formatted tree for the current call stack.
	Stops traversing the stack when encountering files in stop_files.

	Parameters:
	- stop_files (list of str): Filenames at which to stop traversing the stack.
								Defaults to ['app.py', 'main.py'].

	Returns:
	- str: A string representing the formatted call stack tree.
	"""
	if start_files is None:
		start_files = ['app.py', 'routes.py']
	if stop_files is None:
		stop_files = ['Minion.py','app.py']
	if stop_functions is None:
		stop_functions = ['__init__']

	stack = inspect.stack()
	function_tree = ["\n╞🔮 Call Stack:"]
	level = 0
	previous_filename = None
	start = False

	# Iterate through the stack frames, skipping the current frame
	for frame_info in reversed(stack[1:]):
		filename = frame_info.filename.split("/")[-1]
		lineno = frame_info.lineno
		funcname = frame_info.function

		# Check if the current frame's file is in the stop list
		if filename in stop_files:
			continue

		# Check if the current frame's file is in the stop list
		# Enable tree building once a start file is encountered
		if filename in start_files:
			start = True

		if start and '.py' in filename:
			# Determine the indentation level
			if filename != previous_filename:
				current_level = level
				level += 1  # Increase level only when filename changes
				tree = "│  " * current_level
				function_tree.append(f"│  {tree}╭📜 「{filename}」")
			else:
				current_level = level - 1  # Same level as previous
				tree = "│  " * current_level
			if not "module" in funcname:
				function_tree.append(f"│  {tree}╭🪄({lineno}) ⟨{funcname}⟩")
			else:
				function_tree.append(f"│  {tree}╭🪄({lineno})")

		previous_filename = filename

	# Add closing lines based on the final level
	function_tree.append("├" + ("──╯" * level) )
	return "\n".join(function_tree)

def bugged_tree(exc):
	"""
	Builds a visually formatted tree for an exception traceback.
	"""
	tb = exc.__traceback__
	error_tree = ["\n╞🐛 Bugs:"]
	level = 0
	current_level = 0
	previous_filename = None

	while tb:
		frame = tb.tb_frame
		filename = frame.f_code.co_filename.split("/")[-1]
		lineno = tb.tb_lineno
		funcname = frame.f_code.co_name
		tree = "╷  " * current_level

		# Determine if the current frame is from the same file as the previous
		if filename != previous_filename:
			current_level = level
			level += 1
				# Increase level only when filename changes
			error_tree.append(f"╷  {tree}🪲 「{filename}」")
		else:
			current_level = level - 1
				# Same level as previous
		tree = "╷  " * current_level
		error_tree.append(f"╷  {tree}🐞 ({lineno}): ⟨{funcname}⟨⟩")
		previous_filename=filename
		tb = tb.tb_next

	error_tree.append("├" + ("╶╶╯" * level))
	error_tree.append(f"┝🦋 Bug: {type(exc).__name__} - {str(exc)}")
	return "\n".join(error_tree)

def timestamp():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def standard_message( minion = main_minion, message = "", error="", verbose = True):
	'''
	A message with standardized formatting.
	'''
	tree = get_call_tree()
	if not verbose: return f"{minion}\t" + Bold(message) + '\n'+ "\n".join(tree.splitlines()[-3:])
	log_message = ""
	log_message +=    f"{minion} \t"
	log_message +=    f"\n┝✉️\tMessage: "
	splited= Bold(message).splitlines()
	log_message +=    f'\n│ │ '.join(splited)
	log_message +=    f"\n│⏱️\tChronometer:\t{timestamp()}"
	log_message +=    f"\n│🗺️\tAtlas Location: {tree}"
	if error:
		log_message += f"\n┝🛑\tError: {error}"
		log_message += bugged_tree(error)
	log_message +=    f'\n┷'

	return log_message

def Record(message="", error = None, verbose = True):
	"""
	"""
	minion = record_minion
	result = standard_message(
		minion = minion,
		message = Bold(message),
		error = error,
		verbose = verbose,
		)
	Log(Color(result, "Green"))


def News(message="", error = None, verbose = True):
	"""
	Logs an Initialization update message from the News Minion
		Marks Calls.
	"""
	minion = news_minion
	result = standard_message(
		minion = minion,
		message = Bold(message),
		error = error,
		verbose = verbose,
		)
	Log(Color(result, "red"))

def Initialized(message="", error = None):
	return News(message,error)

def Ends(message="", error = None):
	"""
	Logs an Initialization update message from the Ends Minion
		Marks Completion of Calls.
	"""
	minion = ends_minion
	result = standard_message(
		minion = minion,
		message = message,
		error = error
		)
	Log(Color(result, "Red" ))

def Alert(message, error=None):
	"""
	Logs an alert message from the Alert Minion.
	"""
	minion = alert_minion
	result = standard_message(
		minion = minion,
		message = message,
		error = error
		)
	Log(Color(result, "Yellow" ))

def Inform(message, error=None, verbose = True):
	"""
	Logs a general message from the Messenger Minion.
	"""
	minion = messenger_minion
	result = standard_message(
		minion = minion,
		message = message,
		error = None,
		verbose = verbose
		)
	Log(Color(result, "blue" ))

def Warning(message, error=None):
	"""
	Warning message from the Warning Minion.
	🧌: Path Guardian
	"""
	minion = warning_minion
	result = standard_message(
		minion = minion,
		message = message,
		error = None
		)
	Log(Color(result, "Cyan" ))

def Fail(message, error = None):
	"""
	Failure message from the Warning Minion.
	"""
	minion = fail_minion
	result = standard_message(
		minion = minion,
		message = message,
		error = error
		)
	Log(Color(result, "magenta" ))

def Catched(message, error = None):
	minion = data_retrieval_minion
	result = standard_message(
		minion = minion,
		message = message,
		error = error
		)
	Log(Color(result, "green" ))

def generate_bug_tree( exc):
	"""
	Generate a hierarchical bug tree using traceback details.
	Args:
		exc (Exception): The exception to analyze.
	Returns:
		str: Formatted bug tree representation.
	"""
	tb_lines = traceback.format_exception(type(exc), exc, exc.__traceback__)
	stack_summary = traceback.extract_tb(exc.__traceback__)

	tree = "╷\n"
	for entry in stack_summary:
		filename = entry.filename.split("/")[-1]
		line_info = f"({entry.lineno})⟨{entry.name}⟨⟩"
		tree += f"╷  🪲 「{filename}」\n"
		tree += f"╷  🐞 {line_info}\n"

	# Add a final note about the error
	tree += "├╶╶╯╶╶╯╶╶╯╶╶╯"
	return tree

class FailureError(Exception):
	"""Exception raised when an invocation fails."""
	def __init__(self, message = "Invocation Failed", exc=None, minion = fail_minion):
		"""
		Initialize the exception.
		Args:
			message (str): The error message to display.
			exc (Exception): Optional exception to generate a bugged tree.
		"""
		self.bug_tree = generate_bug_tree(exc) if exc else None
		out_message = f"{minion}\n{message}'"
		out_message += f"\n{exc}\n{self.bug_tree}"

		super().__init__(Color(out_message, "Magenta"))


# Test
if __name__ == '__main__':
	setup_logging()
	Log("Test")
	Log(get_call_tree())
	Log(timestamp())
	Log(standard_message(
		message = "Test",
		))
	News("Test")
	Initialized("Test")
	Ends("Test")
	Alert("Test")
	Inform("Test")
	Warning("Test")
	Fail("Test")
	Catched("Test")
