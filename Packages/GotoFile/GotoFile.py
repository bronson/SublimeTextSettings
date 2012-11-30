import sublime, sublime_plugin
import re

# TODO: I really like Open-Include's idea of opening urls too


# expands the selection to a plausible filename and returns the result
def expanded_selection(view, line, left, right):
	pat = re.compile('^[A-Za-z0-9_.-]+$')
	while left > line.begin() and re.match(pat, view.substr(left-1)): left -= 1
	while right < line.end() and re.match(pat, view.substr(right)): right += 1
	return view.substr(sublime.Region(left,right))

def selection_words(view):
	words = []
	for sel in view.sel():
		if sel.empty():
			line = view.line(sel.begin())
			words.append(expanded_selection(view, line, sel.begin(), sel.begin()))
		else:
			words.append(view.substr(sel))
	# print "FILES: " + repr(words)
	return words

class GotoSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command('show_overlay', {'overlay':'goto', 'show_files':True, 'text':selection_words(self.view)[0]})
