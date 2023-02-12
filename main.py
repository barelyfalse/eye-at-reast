def on_clicked(icon, item):
  if str(item) == "Say hello":
    print('Hello world')
  elif str(item) == "Exit":
    icon.stop()

def entry():
  import pystray
  import PIL.Image
  image = PIL.Image.open('eye128.png')
  icon = pystray.Icon("Eye", image, menu=pystray.Menu(
    pystray.MenuItem("Say hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
  ))
  icon.run()

if __name__ == '__main__':
  entry()