# wx tutorial widget
# button

import wx


# create a class without show
# use button in MainFrame to show it
class TextFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pnl = wx.Panel(self)
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='The Central Europe', pos=(130, 15))
        heading.SetFont(font)

        wx.StaticLine(self, pos=(25, 50), size=(300, 1))
        wx.StaticText(self, label='Slovakia', pos=(25, 80))
        wx.StaticText(self, label='Hungary', pos=(25, 100))
        wx.StaticText(self, label='Poland', pos=(25, 120))
        wx.StaticText(self, label='Czech Republic', pos=(25, 140))
        wx.StaticText(self, label='Germany', pos=(25, 160))
        wx.StaticText(self, label='Slovenia', pos=(25, 180))
        wx.StaticText(self, label='Austria', pos=(25, 200))
        wx.StaticText(self, label='Switzerland', pos=(25, 220))

        wx.StaticText(self, label='5 445 000', pos=(250, 80))
        wx.StaticText(self, label='10 014 000', pos=(250, 100))
        wx.StaticText(self, label='38 186 000', pos=(250, 120))
        wx.StaticText(self, label='10 562 000', pos=(250, 140))
        wx.StaticText(self, label='81 799 000', pos=(250, 160))
        wx.StaticText(self, label='2 050 000', pos=(250, 180))
        wx.StaticText(self, label='8 414 000', pos=(250, 200))
        wx.StaticText(self, label='7 866 000', pos=(250, 220))

        wx.StaticLine(self, pos=(25, 260), size=(300, 1))

        tsum = wx.StaticText(self, label='164 336 000', pos=(240, 280))
        sum_font = tsum.GetFont()
        sum_font.SetWeight(wx.BOLD)
        tsum.SetFont(sum_font)
        btn = wx.Button(self, label='Close', pos=(140, 310))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)
        self.SetSize((360, 380))
        self.SetTitle('wx.StaticLine')

    def OnClose(self, e):
        self.Close(True)


# using radio button, check box, spinCtrl combo box, textCtrl
# (1) use self.val to store widgets' values, change their corresponding values when EVT_(widget)
# (2) get widget value by calling self.widget.GetValue()
class PrivateInfoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pnl = wx.Panel(self)
        # static box for bounding all widgets
        wx.StaticBox(pnl, label='Personal Info', pos=(5, 5), size=(240, 170))
        # member value
        self.age = 40 # SpinCtrl
        self.smoke = False # check box
        self.gender = 'Male' # radio button
        self.income = 20  # slider
        # radio buttons
        self.mcb = wx.RadioButton(pnl, label='Male', pos=(15, 30))
        self.fcb = wx.RadioButton(pnl, label='Female', pos=(15, 55))
        self.mcb.SetValue(self.gender == 'Male')
        self.mcb.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton)
        self.fcb.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton)
        # SpinCtrl
        asp = wx.SpinCtrl(pnl, value='1', pos=(55, 90), size=(60, -1), min=1, max=120)
        asp.SetValue(self.age)
        asp.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl)
        wx.StaticText(pnl, label='Age', pos=(15, 95))
        # CheckBox
        scb = wx.CheckBox(pnl, label='Smoke', pos=(80, 30))
        scb.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        scb.SetValue(self.smoke)
        btn = wx.Button(pnl, label='Ok', pos=(90, 185), size=(60, -1))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)
        # combo box
        jobs = ['Researcher', 'Architecture', 'Doctor', 'Engineer', 'Others']
        self.jcb = wx.ComboBox(pnl, pos=(120,60), choices=jobs, style=wx.CB_READONLY | wx.CB_DROPDOWN)
        self.tc = wx.TextCtrl(pnl, pos=(120, 90))
        self.tc.Hide()
        # slider
        sld = wx.Slider(pnl, value=20, minValue=15, maxValue=55, style=wx.SL_HORIZONTAL, pos=(25, 120), size=(250,-1))
        sld.Bind(wx.EVT_SLIDER, self.OnSlider)
        self.st_sld = wx.StaticText(pnl, label='Income=' + str(self.income), pos=(25, 150))
        self.SetSize((300, 250))
        self.SetTitle('Static box')
        self.Centre()

    def OnSlider(self, e):
        obj = e.GetEventObject()
        self.income = obj.GetValue()
        self.st_sld.SetLabel(u'Income=%d' % self.income)


    def OnJob(self, e):
        job = e.GetEventObject().GetValue()
        self.job = job
        if job != 'Others':
            self.tc.Hide()
        else:
            self.tc.Show()

    def OnCheckBox(self, e):
        if e.GetEventObject().GetValue():
            self.smoke = True
        else:
            self.smoke = False

    def OnRadioButton(self, e):
        if self.mcb.GetValue():
            self.gender = 'Male'
        else:
            self.gender = 'Female'

    def OnSpinCtrl(self, e):
        self.age = e.GetEventObject().GetValue()

    def OnClose(self, e):
        str_smoke = ''
        if self.smoke:
            str_smoke = 'Smoking'
        else:
            str_smoke = 'No smoking'
        job = self.jcb.GetValue()
        if job == 'Others':
            job = self.tc.GetValue()
        wx.MessageBox('%s/%d (%s) : %s' % (self.gender, self.age, str_smoke, job))
        self.Close(True)


TASK_RANGE = 50


class GaugeFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = wx.Timer(self, 1)
        self.count = 0
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(pnl, range=TASK_RANGE, size=(250, 50))
        self.btn1 = wx.Button(pnl, wx.ID_OK)
        self.btn2 = wx.Button(pnl, wx.ID_STOP)
        self.text = wx.StaticText(pnl, label='Task to be done')

        self.Bind(wx.EVT_BUTTON, self.OnOk, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.btn2)

        hbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)
        hbox2.Add(self.btn2, proportion=1)
        hbox3.Add(self.text, proportion=1)
        vbox.Add((0, 30))
        vbox.Add(hbox1, flag=wx.ALIGN_CENTRE)
        vbox.Add((0, 20))
        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox3, proportion=1, flag=wx.ALIGN_CENTRE)

        pnl.SetSizer(vbox)

        self.SetSize((300, 200))
        self.SetTitle('wx.Gauge')
        self.Centre()

    def OnOk(self, e):
        if self.count >= TASK_RANGE:
            return
        self.timer.Start(100)
        self.text.SetLabel('Task in Progress')

    def OnStop(self, e):
        if self.count == 0 or self.count >= TASK_RANGE or not self.timer.IsRunning():
            return
        self.timer.Stop()
        self.text.SetLabel('Task Interrupted')

    def OnTimer(self, e):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)  # progress
        if self.count == TASK_RANGE:
            self.timer.Stop()
            self.text.SetLabel('Task Completed')


# it seems ID no meaning
# just bind handler to widget
# no info. for one handler to deal with more than one IDs' widgets
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        # normal button
        cbtn = wx.Button(pnl, label='Close', pos=(25,10))
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)
        # toggle button
        self.col = wx.Colour(0,0,0)
        rtb = wx.ToggleButton(pnl, label='Red', pos=(25, 50)) # local value within {}
        gtb = wx.ToggleButton(pnl, label='Green', pos=(25, 80))
        btb = wx.ToggleButton(pnl, label='Blue', pos=(25, 110))
        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleBlue)
        self.cpnl = wx.Panel(pnl, pos=(140, 20), size=(100,100)) #self.name: instance member value
        self.cpnl.SetBackgroundColour(self.col)
        # static text
        cbtn1 = wx.Button(pnl, label='Text', pos=(25, 140))
        cbtn1.Bind(wx.EVT_BUTTON, self.OnShowTextFrame)
        # private info. Frame
        cbtn2 = wx.Button(pnl, label='prvivate Info.', pos=(25, 170))
        cbtn2.Bind(wx.EVT_BUTTON, self.OnShowRadioFrame)
        # Gauge frame
        cbtn3 = wx.Button(pnl, label='Gauge', pos=(25, 200))
        cbtn3.Bind(wx.EVT_BUTTON, self.OnGauge)

        self.SetSize((300, 300))
        self.SetTitle('widgets')
        self.Center()
        self.Show(True)

    def OnGauge(self, e):
        gf = GaugeFrame(None)
        gf.Show(True)

    def OnShowRadioFrame(self, e):
        rbf = PrivateInfoFrame(None)
        rbf.Show(True)

    def OnShowTextFrame(self, e):
        tf = TextFrame(None)
        tf.Show(True)

    def ToggleRed(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        green = self.col.Green()
        blue = self.col.Blue()
        if isPressed:
            self.col = wx.Colour(255, green, blue)
        else:
            self.col = wx.Colour(0, green, blue)
        self.cpnl.SetBackgroundColour(self.col)
        self.Refresh()

    def ToggleGreen(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        red = self.col.Red()
        blue = self.col.Blue()
        if isPressed:
            self.col = wx.Colour(red, 255, blue)
        else:
            self.col = wx.Colour(red, 0, blue)
        self.cpnl.SetBackgroundColour(self.col)
        self.Refresh()

    def ToggleBlue(self, e):
        obj = e.GetEventObject()

        isPressed = obj.GetValue()
        red = self.col.Red()
        green = self.col.Green()
        if isPressed:
            self.col = wx.Colour(red, green, 255)
        else:
            self.col = wx.Colour(red, green, 255)
        self.cpnl.SetBackgroundColour(self.col)
        self.Refresh()

    def OnClose(self, e):
        self.Close(True)



def main():
    ex = wx.App()
    MyFrame(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()




