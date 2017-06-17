# wx tutorial event
# bind handler to event
# bind handler to event with a specified ID (a specified widget)

import wx


class MyWindow(wx.Panel):
    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)

        self.color = '#b3b3b3'

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, e):
        self.Refresh()

    def OnSetFocus(self, e):  # Ctrl+TAB to change focus
        self.color = '#0099f7'
        self.Refresh()

    def OnKillFocus(self, e):
        self.color = '#b3b3b3'
        self.Refresh()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.InitU()

    def InitU(self):
        self.statusbar = self.CreateStatusBar()
        #self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMove)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        panel = wx.Panel(self)
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.LEFT, 9),
                      (MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.RIGHT, 9),
                      (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.LEFT, 9),
                      (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 9)])
        self.SetSizer(grid)

        self.SetSize((250, 180))
        self.SetTitle('Move event')
        self.Centre()
        self.Show(True)

    def OnMove(self, e):
        x, y = e.GetPosition()
        self.statusbar.SetStatusText(u'start:(%d,%d)' % (x, y))

    def OnCloseWindow(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                             wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()  # cancel the event

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()