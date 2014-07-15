#!/usr/bin/env python
# -*- coding: gbk -*- 

from wx import wx

class Frame(wx.Frame):
    pass

class App(wx.App):
    
    _win = None
    _panel = None
    
    infoText = None
    
    def main(self):
        app=wx.App()  
        #win=wx.Frame(None,-1,'Icon',wx.DefaultPosition,wx.Size(350,300))
        self._win=wx.Frame(None, title="帕斯婷SSO系统上线工具", size=(700,300))  
        #frame.SetIcon(wx.Icon('ico.ico',wx.BITMAP_TYPE_ICO))
        
        self._panel = wx.Panel(self._win)
        
        title = wx.StaticText(self._panel, label="帕斯婷SSO系统上线工具",)
        font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD)  
        title.SetFont(font)
        hr = wx.StaticLine(self._panel,1,style=wx.LI_HORIZONTAL)
        hr1 = wx.StaticLine(self._panel,1,style=wx.LI_HORIZONTAL)
               
        stopBtn =       wx.Button(self._panel, 10001, label="1 停止服务")
        backupBtn =     wx.Button(self._panel, 10002, label="2 备份代码")
        buildBtn =      wx.Button(self._panel, 10003, label="3 更新代码")
        startBtn =      wx.Button(self._panel, 10004, label="4 启动服务")
        restartBtn =    wx.Button(self._panel, 10005, label="0 重启服务")
        
        self._win.Bind(wx.EVT_BUTTON, self.btnClick, stopBtn)
        self._win.Bind(wx.EVT_BUTTON, self.btnClick, backupBtn)
        self._win.Bind(wx.EVT_BUTTON, self.btnClick, buildBtn)
        self._win.Bind(wx.EVT_BUTTON, self.btnClick, startBtn)
        self._win.Bind(wx.EVT_BUTTON, self.btnClick, restartBtn)
        
        self.infoText = wx.TextCtrl(self._panel,style=wx.TE_MULTILINE | wx.HSCROLL)
        self.infoText.SetValue("操作之前，请确保要更新的 war 文件名为 sso.war，并上传至 ftp 目录。\n")
                               
        tbox = wx.BoxSizer(wx.VERTICAL)
        tbox.Add(title, proportion=1, flag=wx.ALIGN_CENTER)
        tbox.Add(hr, proportion=0, flag=wx.EXPAND)
        
        cbox = wx.BoxSizer()
        cbox.Add(stopBtn,proportion=0)
        cbox.Add(backupBtn,proportion=0)
        cbox.Add(buildBtn,proportion=0)
        cbox.Add(startBtn,proportion=0)
        cbox.Add(restartBtn,proportion=0)   
        
        bbox = wx.BoxSizer(wx.VERTICAL)
        bbox.Add(tbox, proportion=0, flag=wx.EXPAND)
        bbox.Add(cbox, proportion=0, flag=wx.CENTER)
        bbox.Add(hr1, proportion=0, flag=wx.EXPAND)
        bbox.Add(self.infoText, proportion=1, flag=wx.EXPAND)
        
        self._panel.SetSizer(bbox)

        self._win.Center() 
        self._win.Show()
    
        app.MainLoop()
         
    def checkIdValMap(self, ids):
        if 10001==ids: return "stop"
        if 10002==ids: return "backup"
        if 10003==ids: return "build"
        if 10004==ids: return "start"
        if 10005==ids: return "restart"
    
    def btnClick(self, event):
        dlg=wx.MessageDialog(None,"确定提交吗?","提示信息",wx.YES_NO|wx.ICON_QUESTION)
        retCode = dlg.ShowModal()
        if (retCode == wx.ID_YES):
            sender = event.GetEventObject()
            ids = self.checkIdValMap(sender.GetId())
            #print ids
            self.runSocket(ids)
            #self.saveBtn.Enable(True)
        dlg.Destroy()

    def runSocket(self, cmd):
        text = 'root|'+cmd
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.setdefaulttimeout(10)
        try:
            sock.connect(('192.168.77.200', 8001))
            sock.send(text)  
            bufs = sock.recv(10024)
            bufs = bufs.replace('\\r\\n', '').replace('\'', '').replace('[', '').replace(']', '').replace('\\n', '').replace('\\r', '')
            self.infoText.SetValue(self.infoText.GetValue()+"\n"+bufs)
        #except socket.error, arg:
        #        (errno, err_msg) = arg
        #        msg = "服务器连接失败: %s, errno=%d, 请关闭程序后重新打开连接" % (err_msg, errno)
        except:
            msg = "服务器连接失败, 请关闭程序后重新打开连接"
            self.infoText.SetValue(msg)
        sock.close()


if __name__ == '__main__':  
    App().main()

