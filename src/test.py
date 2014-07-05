#!/usr/bin/env python
# coding: utf-8

from wx import wx

class App(wx.App):
    
    _win = None
    _panel = None
    
    checked = []
    infoText = None
    saveBtn = None
    
    def main(self):
        app=wx.App()  
        self._win=wx.Frame(None, title="帕斯婷系统上线工具", size=(600,400))  
        
        self._panel = wx.Panel(self._win)
        self.infoText = wx.TextCtrl(self._panel,style=wx.TE_MULTILINE | wx.HSCROLL) 
        
        bbox = wx.BoxSizer(wx.VERTICAL)
        bbox.Add(self.infoText, proportion=1, flag=wx.EXPAND)
        
        self._panel.SetSizer(bbox)

        self._win.Center() 
        self._win.Show()
    
        '''
        wx.Button(win, label="open",pos=(225,5), size=(80,25))
        wx.Button(win, label="save",pos=(315,5), size=(80,25))
        wx.TextCtrl(win, pos=(5,35), size=(575,300), style=wx.TE_MULTILINE | wx.HSCROLL)
        '''
        app.MainLoop()
        


if __name__ == '__main__':  
    App().main()


    