# wx tutorial dialog
# message box:
# dialog box
# about box: not supported by cocoa
# custom box: I put it into help menu

import wx


class ChangeDepthDialog(wx.Dialog):
    def __init__(self, *args, **kw):
        super(ChangeDepthDialog, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((250, 200))
        self.SetTitle("Change Color Depth")

    def InitUI(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(pnl, label='Colors')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(pnl, label='256 Colors',
                               style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(pnl, label='16 Colors'))
        sbs.Add(wx.RadioButton(pnl, label='2 Colors'))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(pnl, label='Custom'))
        hbox1.Add(wx.TextCtrl(pnl), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1,
                 flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2,
                 flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnClose(self, e):
        self.Destroy()

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        wx.CallLater(5000, self.ShowMessage) # postpone 5 secs
        # add grid sizer buttons
        panel = wx.Panel(self)
        hbox = wx.BoxSizer()
        sizer = wx.GridSizer(2, 2, 2, 2)
        btn1 = wx.Button(panel, label='Info')
        btn2 = wx.Button(panel, label='Error')
        btn3 = wx.Button(panel, label='Question')
        btn4 = wx.Button(panel, label='Alert')
        sizer.AddMany([btn1, btn2, btn3, btn4])
        hbox.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizer(hbox)
        btn1.Bind(wx.EVT_BUTTON, self.ShowMessage1)
        btn2.Bind(wx.EVT_BUTTON, self.ShowMessage2)
        btn3.Bind(wx.EVT_BUTTON, self.ShowMessage3)
        btn4.Bind(wx.EVT_BUTTON, self.ShowMessage4)

        menu = wx.MenuBar()
        help = wx.Menu()
        help.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id = 100)
        menu.Append(help, '&Help\tCtrl+H')
        self.SetMenuBar(menu)

        self.SetSize((300, 200))
        self.SetTitle('Message box')
        self.Centre()
        self.Show(True)

    def OnAboutBox(self, e):
        chgdep = ChangeDepthDialog(None, title='Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()

    def ShowMessage(self):
        wx.MessageBox('Download completed', 'Info',
                      wx.OK | wx.ICON_INFORMATION)

    def ShowMessage1(self, event):
        dial = wx.MessageDialog(None, 'Download completed', 'Info', wx.OK)
        dial.ShowModal()

    def ShowMessage2(self, event):
        dial = wx.MessageDialog(None, 'Error loading file', 'Error',
                                wx.OK | wx.ICON_ERROR)
        dial.SetIcon(wx.Icon('exit.png', wx.BITMAP_TYPE_PNG))  # not effect
        dial.ShowModal()

    def ShowMessage3(self, event):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        dial.ShowModal()

    def ShowMessage4(self, event):
        dial = wx.MessageDialog(None, 'Unallowed operation', 'Exclamation',
                                wx.OK | wx.ICON_EXCLAMATION)
        dial.ShowModal()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()