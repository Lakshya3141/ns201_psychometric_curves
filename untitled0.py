from psychopy import visual, core
#win = visual.Window([400,400])
win = visual.Window(fullscr=True,color=(-1, -1, -1))
message = visual.TextStim(win, text='hello')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(5)
message.text = 'world'  # Change properties of existing stim
win.flip()
core.wait(5)
win.close()
core.quit()