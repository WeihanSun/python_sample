#!/usr/bin/python

# simple.py
# Show a frame with menu bar, toolbar, status bar, pop menu

import wx

# popup menu class
class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Maximum')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnMaximize, cmi)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnMaximize(self, e):
        self.parent.Maximize()


# Frame class
APP_EXIT = 1
class Example_Frame(wx.Frame):
    def __init__(self, parent, title):
        super(Example_Frame, self).__init__(parent, title=title,
                                      size=(250, 200))
        self.initUI()

    def initUI(self):
        menubar = wx.MenuBar() # create a menubar instance
        # --- the first menu ---
        fileMenu = wx.Menu()  # create a menu instance
        fitem = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q') # create a menuitem with an ID
        img = wx.Image('exit.bmp') # load an image (64x64)
        img = img.Scale(16, 16) # resize the image
        fitem.SetBitmap(wx.Bitmap(img)) # set to the menuitem
        fileMenu.Append(fitem) # add menuitem to menu
        self.Bind(wx.EVT_MENU, self.OnQuit, id = APP_EXIT) # bind the menuitem to menuitem ID
        # = self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        menubar.Append(fileMenu, '&File') # add menu to menubar

        # --- the second menu with a sub menu ----
        editMenu = wx.Menu()
        editMenu.Append(wx.ID_COPY, '&Copy\tCtrl+C')
        editMenu.Append(wx.ID_PASTE, '&Paste\tCtrl+P')
        editMenu.AppendSeparator()
        # sub menu
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')
        editMenu.Append(wx.ID_ANY, 'I&mport', imp)
        menubar.Append(editMenu, '&Edit')

        # ---  the third menu with checkbox menu items connected to toolbar and statusbar ---
        viewMenu = wx.Menu()
        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Show Status Bar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Show Tool Bar', kind=wx.ITEM_CHECK)
        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)
        menubar.Append(viewMenu, '&View')

        self.SetMenuBar(menubar) # add menubar to frame
        # add toolbar
        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(wx.ID_ANY, '', wx.Bitmap('new.bmp'))
        self.toolbar.AddTool(wx.ID_EXIT, '', wx.Bitmap('exit.bmp'))
        self.toolbar.EnableTool(wx.ID_EXIT, False)
        self.toolbar.Realize()
        # add status bar
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')
        # bind right down
        self.popMenu = MyPopupMenu(self)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    def OnQuit(self, e):
        self.Close()

    def show(self):
        self.Center()
        self.Move((800, 250))
        self.Show()

    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def OnRightDown(self, e):
        self.PopupMenu(self.popMenu, e.GetPosition())

if __name__ == '__main__':
    # must have App()
    app = wx.App()
    # wx.Frame(wx.Window parent, int id=-1, string title='', wx.Point pos = wx.DefaultPosition,
    #  wx.Size size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, string name = "frame")
#    frame = wx.Frame(None, style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
#                               | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
#    frame.Show()

    # sample of using Eample class
    ef = Example_Frame(None, title='Size')
    Example_Frame.show(ef)
    app.MainLoop()
