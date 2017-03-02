# coding=utf8
import os, sublime, sublime_plugin, glob, subprocess


# Constants
CODE_DIR = os.environ['CODE_DIR'] + '/'


class SwitchCommand(sublime_plugin.WindowCommand):

  def run(self):
    repos = self.get_dir_names()
    self.window.show_quick_panel(repos, self.on_select, sublime.KEEP_OPEN_ON_FOCUS_LOST, 0, None)

  def on_select(self, selected):
    if selected == -1:
      return
    repo = self.get_dir_names()[selected]
    repo_path = CODE_DIR + repo
    self.openInNewWindow(repo_path)

  def get_dir_names(self):
    code_dir = CODE_DIR + '*/'
    repos_full = glob.glob(code_dir)
    repos = []
    for path in repos_full:
      repos.append(path.split('/')[-2])
    return repos

  def openInNewWindow(self, path):
    try:
      subprocess.Popen(['sub', '.'], cwd=path)
    except:
      try:
        subprocess.Popen(['subl', '.'], cwd=path)
      except:
        try:
          subprocess.Popen(['sublime', '.'], cwd=path)
        except:
          subprocess.Popen(['/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl', '.'], cwd=path)

