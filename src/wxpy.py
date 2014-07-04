#!/usr/bin/env python
# coding: utf-8

from wx import wx

def main():
    app=wx.App()  
    #win=wx.Frame(None,-1,'Icon',wx.DefaultPosition,wx.Size(350,300))
    win=wx.Frame(None, title="帕斯婷系统上线工具", size=(600,400))  
    #frame.SetIcon(wx.Icon('ico.ico',wx.BITMAP_TYPE_ICO))
    
    bkg = wx.Panel(win)
    
    title = wx.StaticText(bkg, label="帕斯婷系统上线工具")
    font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD)  
    title.SetFont(font)
    hr = wx.StaticLine(bkg,1,style=wx.LI_HORIZONTAL)
    
    devCheck = wx.CheckBox(bkg, label="dev.(skin/mall).ptp.cn [手机端]")
    skinCheck = wx.CheckBox(bkg, label="(skin/mall).ptp.cn [手机端]")
    aboutCheck = wx.CheckBox(bkg, label="about.ptp.cn")
    brandCheck = wx.CheckBox(bkg, label="brand.ptp.cn")
    wwwCheck = wx.CheckBox(bkg, label="www.ptp.cn")
        
    win.Bind(wx.EVT_CHECKBOX,ONCheck)
    
    saveBtn = wx.Button(bkg, label="提交")
    infoText = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)
    
    tbox = wx.BoxSizer(wx.VERTICAL)
    tbox.Add(title, proportion=0, flag=wx.ALIGN_CENTER)
    tbox.Add(hr, proportion=0, flag=wx.EXPAND)
    
    cbox = wx.BoxSizer(wx.VERTICAL)
    cbox.Add(devCheck,proportion=0)
    cbox.Add(skinCheck,proportion=0)
    cbox.Add(aboutCheck,proportion=0)
    cbox.Add(brandCheck,proportion=0)
    cbox.Add(wwwCheck,proportion=0)
   
    hbox = wx.BoxSizer(wx.VERTICAL)
    hbox.Add(tbox, proportion=0)
    hbox.Add(cbox, proportion=0)
    hbox.Add(saveBtn,proportion=0, flag=wx.RIGHT, border=5)
    
    bbox = wx.BoxSizer(wx.VERTICAL)
    bbox.Add(hbox, proportion=0)
    bbox.Add(infoText, proportion=1, flag=wx.EXPAND)
    
    bkg.SetSizer(bbox)
    
    win.Show()
    
    

    '''
    win.Center()  
    win.Show() 
    wx.Button(win, label="open",pos=(225,5), size=(80,25))
    wx.Button(win, label="save",pos=(315,5), size=(80,25))
    wx.TextCtrl(win, pos=(5,35), size=(575,300), style=wx.TE_MULTILINE | wx.HSCROLL)
    '''
    app.MainLoop()
    
def ONCheck(evt):
    print evt.SetValue(evt.IsChecked())

if __name__ == '__main__':  
    main()


    