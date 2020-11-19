#!/usr/bin/env Python
# completely functional wxpython calculator

import wx


class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title=title, size=(300, 400))

        # show window on screen
        self.setup()
        self.Show()

    def setup(self):
        box = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridSizer(5, 4, 10, 10)

        # add textbox for output
        self.textbox = wx.TextCtrl(self, style=wx.TE_RIGHT)
        box.Add(self.textbox, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]

        # create buttons
        for label in buttons:
            button = wx.Button(self, -1, label)
            grid.Add(button, 0, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.on_button_press, button)

        box.Add(grid, proportion=1, flag=wx.EXPAND)
        self.SetSizer(box)

    def on_button_press(self, e):

        label = e.GetEventObject().GetLabel()

        calculation = self.textbox.GetValue()

        # handle event based on what button is pressed
        if label == '=':
            if not calculation:
                return

            try:
                result = eval(calculation)
            except SyntaxError as err:
                wx.LOG_Error('Invalid syntax ({}). Please check your input and try again.'.format(calculation))
                return
            except NameError as err:
                wx.LOG_Error('There was an error. Please check your input and try again.')
                return

            # show result
            self.textbox.SetValue(str(result))

        elif label == 'C':  # clear if C
            self.textbox.SetValue('')
        else:  # 0-9
            self.textbox.SetValue(calculation + label)  # add the label of btn to calculation


if __name__ == '__main__':
    # create application object
    app = wx.App()
    Interface(None, title='Calculator')

    app.MainLoop()

