import os
import subprocess

def find_apps():
  """Searched all apps and output their paths"""
  apps = []
  for root, dirs, files in os.walk("/"):
    for file in files:
      if file.endswith((".exe", ".lnk", ".app")):  # Добавьте другие расширения, если нужно
        app_path = os.path.join(root, file)
        apps.append(app_path)
  return apps

def display_apps(apps):
  """Output the list of applications"""
  print("Searched apps:")
  for i, app in enumerate(apps):
    print(f"{i+1}. {os.path.basename(app)}")

def launch_app(apps):
  """Run application."""
  choice = input("Enter application number or 'q' to exit: ")
  if choice.lower() == 'q':
    return False
  try:
    app_index = int(choice) - 1
    if 0 <= app_index < len(apps):
      subprocess.run([apps[app_index]])
    else:
      print("Wrong number!")
  except ValueError:
    print("Enter application number or 'q' to exit: ")
  return True

if __name__ == "__main__":
  apps = find_apps()
  display_apps(apps)

  # Цикл для запуска приложений
  while True:
    if not launch_app(apps):
      break
