#!/usr/bin/env python
# coding: utf-8

from wx import wx

class Frame(wx.Frame):
    pass

class App(wx.App):
    
    _win = None
    _panel = None
    
    checked = []
    infoText = None
    saveBtn = None
    
    def main(self):
        app=wx.App()  
        #win=wx.Frame(None,-1,'Icon',wx.DefaultPosition,wx.Size(350,300))
        self._win=wx.Frame(None, title="帕斯婷系统上线工具", size=(600,400))  
        #frame.SetIcon(wx.Icon('ico.ico',wx.BITMAP_TYPE_ICO))
        
        self._panel = wx.Panel(self._win)
        
        title = wx.StaticText(self._panel, label="帕斯婷系统上线工具",)
        font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD)  
        title.SetFont(font)
        hr = wx.StaticLine(self._panel,1,style=wx.LI_HORIZONTAL)
        hr1 = wx.StaticLine(self._panel,1,style=wx.LI_HORIZONTAL)
        
        devCheck = wx.CheckBox(self._panel, 10001, label="dev.(skin/mall).ptp.cn [手机端]  ")
        devCheck.SetValue(False)
        skinCheck = wx.CheckBox(self._panel, 10002, label="(skin/mall).ptp.cn [手机端]  ")
        skinCheck.SetValue(False)
        aboutCheck = wx.CheckBox(self._panel, 10003, label="about.ptp.cn  ")
        aboutCheck.SetValue(False)
        brandCheck = wx.CheckBox(self._panel, 10004, label="brand.ptp.cn  ")
        brandCheck.SetValue(False)
        wwwCheck = wx.CheckBox(self._panel, 10005, label="www.ptp.cn")
        wwwCheck.SetValue(False)
        self._win.Bind(wx.EVT_CHECKBOX, self.ONCheck)
        
        
        self.saveBtn = wx.Button(self._panel, label="提交")
        self._win.Bind(wx.EVT_BUTTON, self.saveBtnClick, self.saveBtn)
        self.infoText = wx.TextCtrl(self._panel,style=wx.TE_MULTILINE | wx.HSCROLL)
        
        tbox = wx.BoxSizer(wx.VERTICAL)
        tbox.Add(title, proportion=1, flag=wx.ALIGN_CENTER)
        tbox.Add(hr, proportion=0, flag=wx.EXPAND)
        
        cbox = wx.BoxSizer()
        cbox.Add(devCheck,proportion=0)
        cbox.Add(skinCheck,proportion=0)
        cbox.Add(aboutCheck,proportion=0)
        cbox.Add(brandCheck,proportion=0)
        cbox.Add(wwwCheck,proportion=0)   
        
        bbox = wx.BoxSizer(wx.VERTICAL)
        bbox.Add(tbox, proportion=0, flag=wx.EXPAND)
        bbox.Add(cbox, proportion=0, flag=wx.CENTER)
        bbox.Add(hr1, proportion=0, flag=wx.EXPAND)
        bbox.Add(self.saveBtn,proportion=0, flag=wx.CENTER, border=5)
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
        
    def ONCheck(self,e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        if isChecked:
            self.checked.append(self.checkIdValMap(sender.GetId()))
        else: 
            self.checked.remove(self.checkIdValMap(sender.GetId()))
    
    def checkIdValMap(self, id):
        if 10001==id: return ("dev.skin.ptp.cn","dev/skin.ptp.cn")
        if 10002==id: return ("skin.ptp.cn","skin.ptp.cn")
        if 10003==id: return ("about.ptp.cn","about.ptp.cn")
        if 10004==id: return ("brand.ptp.cn","brand.ptp.cn")
        if 10005==id: return ("www.ptp.cn","www.ptp.cn")
    
    def saveBtnClick(self, event):
        dlg=wx.MessageDialog(None,"确定提交吗?","提示信息",wx.YES_NO|wx.ICON_QUESTION)
        retCode = dlg.ShowModal()
        if (retCode == wx.ID_YES):
            self.saveBtn.Enable(False)
            self.runSocket()
        dlg.Destroy()

    def runSocket(self):
        text = ''
        i=1
        for lists in self.checked:
            text = text+','.join(lists)
            if i<len(self.checked): text = text + "|"
            i=i+1
        if not text:
            self.saveBtn.Enable(True)
            return False
        #print text

        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(10)
        try:
            sock.connect(('192.168.77.200', 8001))
            sock.send(text)  
            bufs = sock.recv(1024)
            i=0
            for buf in bufs.split(","):
                i=i+1
                if 3>=i: continue
                msg = buf.replace('\\r\\n', '').replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '')
                self.infoText.SetValue(self.infoText.GetValue()+"\n"+msg)
                self.saveBtn.Enable(True)
        except socket.error, arg:
                (errno, err_msg) = arg
                msg = "服务器连接失败: %s, errno=%d, 请关闭程序后重新打开连接" % (err_msg, errno)
                self.infoText.SetValue(msg)
                #self.saveBtn.Enable(True)
        sock.close()


if __name__ == '__main__':  
    App().main()


    