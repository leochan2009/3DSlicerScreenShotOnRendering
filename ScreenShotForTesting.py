""" Allow to associate a python function called following the 'EndEvent' coming from 
a given ThreeD renderer managed by Slicer layout manager.

Usage:
  
  # Install screenshot grabber
  id = install_threed_view_action(takeScreenshot)
  
  # Move threeD view around
  
  # Uninstall screenshot grabber
  uninstall_threed_view_action(id)
"""


import datetime
import time
class ScreenShotForTesting:
  def __init__(self):
    self.id = 0
    self.screenshotID = 0
    self.screenshot_path = 'C:\\Users\\leochan\\Desktop\\QiaoJu'
    self.screenshot_prefix = 'screenshot_'
    self.lm = slicer.app.layoutManager()
    self.viewWidget = self.lm.threeDWidget(0)
    self.view = self.viewWidget.threeDView()
    self.rw = self.view.renderWindow()
    self.interactor = self.view.interactor()
    
  def takeScreenshot(self, rw, event):
    import os
    import datetime as dt
    import time
    ms_since_epoch = datetime.datetime.now().strftime('%m%d%H%M%S%f')
    filename = self.screenshot_prefix + str(ms_since_epoch) + '.png'
    filepath = os.path.join(self.screenshot_path, filename)
    self.screenshotID = self.screenshotID + 1
    print("screenshot:%s" % event) # Not implemented
    self.rw.RemoveObserver(self.id)
    wti=vtk.vtkWindowToImageFilter()
    wti.SetInput(self.rw)
    wti.Update()
    writer=vtk.vtkPNGWriter()
    writer.SetFileName(filepath)
    writer.SetInputConnection(wti.GetOutputPort())
    writer.Write()
    slicer.app.processEvents()
    self.Run()
    
  def Run(self):
    #self.id = self.interactor.AddObserver('LeftButtonPressEvent', self.takeScreenshot)
    #self.id = self.interactor.AddObserver('MouseMoveEvent', self.takeScreenshot)
    self.id = self.rw.AddObserver('RenderEvent', self.takeScreenshot)
    #self.id = self.install_threed_view_action(self.takeScreenshot)

a = ScreenShotForTesting()
a.Run()