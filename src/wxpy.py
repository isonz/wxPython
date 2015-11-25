#!/usr/bin/env python
# -*- coding: gbk -*- 

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
        self._win=wx.Frame(None, title="��˹��ϵͳ���߹���", size=(800,300))  
        #frame.SetIcon(wx.Icon('ico.ico',wx.BITMAP_TYPE_ICO))
        
        self._panel = wx.Panel(self._win)
        
        title = wx.StaticText(self._panel, label="��˹��ϵͳ���߹���",)
        font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD)  
        title.SetFont(font)
        hr = wx.StaticLine(self._panel,1,style=wx.LI_HORIZONTAL)
        hr1 = wx.StaticLine(self._panel,1,style=wx.LI_HORIZONTAL)
        
        wwwCheck = wx.CheckBox(self._panel, 10001, label="www.ptp.cn")
        wwwCheck.SetValue(False)
        devCheck = wx.CheckBox(self._panel, 10002, label="dev.placentin.com/erase")
        devCheck.SetValue(False)
        wwwpstCheck = wx.CheckBox(self._panel, 10003, label="www.placentin.com")
        wwwpstCheck.SetValue(False)
        adminCheck = wx.CheckBox(self._panel, 10004, label="admins.placentin.com.cn")
        adminCheck.SetValue(False)
        FXCheck = wx.CheckBox(self._panel, 10005, label="fx.ptp.cn")
        FXCheck.SetValue(False)
        FXAdminCheck = wx.CheckBox(self._panel, 10006, label="admin.fx.ptp.cn")
        FXAdminCheck.SetValue(False)
        self._win.Bind(wx.EVT_CHECKBOX, self.ONCheck)
        
        
        self.saveBtn = wx.Button(self._panel, label="�ύ")
        self._win.Bind(wx.EVT_BUTTON, self.saveBtnClick, self.saveBtn)
        self.infoText = wx.TextCtrl(self._panel,style=wx.TE_MULTILINE | wx.HSCROLL)
        
        tbox = wx.BoxSizer(wx.VERTICAL)
        tbox.Add(title, proportion=1, flag=wx.ALIGN_CENTER)
        tbox.Add(hr, proportion=0, flag=wx.EXPAND)
        
        cbox = wx.BoxSizer()
        cbox.Add(devCheck,proportion=0)
        cbox.Add(FXCheck,proportion=0)
        cbox.Add(wwwCheck,proportion=0)
        cbox.Add(wwwpstCheck,proportion=0)
        
        apbox = wx.BoxSizer()
        apbox.Add(adminCheck,proportion=0)
        apbox.Add(FXAdminCheck,proportion=0)
        
        bbox = wx.BoxSizer(wx.VERTICAL)
        bbox.Add(tbox, proportion=0, flag=wx.EXPAND)
        #bbox.Add(cbox, proportion=0, flag=wx.CENTER)
        bbox.Add(cbox, proportion=0, flag=wx.LEFT)
        bbox.Add(apbox, proportion=0, flag=wx.LEFT)
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
    
    def checkIdValMap(self, ids):
        if 10001==ids: return ("www.ptp.cn","www.ptp.cn")
        if 10002==ids: return ("dev.placentin.com_erase","dev/erase")
        if 10003==ids: return ("www.placentin.com","www.placentin.com")
        if 10004==ids: return ("admins.placentin.com.cn","admins.placentin.com.cn")
        if 10005==ids: return ("fx.ptp.cn","fx.ptp.cn")
        if 10006==ids: return ("admin.fx.ptp.cn","admin.fx.ptp.cn")
    
    def saveBtnClick(self, event):
        dlg=wx.MessageDialog(None,"ȷ���ύ��?","��ʾ��Ϣ",wx.YES_NO|wx.ICON_QUESTION)
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
        #socket.setdefaulttimeout(10)
        try:
            sock.connect(('192.168.75.200', 8001))
            sock.send(text)  
            bufs = sock.recv(10024)
            i=0
            for buf in bufs.split(","):
                i=i+1
                #if 3>=i: continue
                msg = buf.replace('\\r\\n', '').replace('\'', '').replace('[', '').replace(']', '').replace('\\n', '').replace('\\r', '')
                self.infoText.SetValue(self.infoText.GetValue()+"\n"+msg)
                self.saveBtn.Enable(True)
        #except socket.error, arg:
        #        (errno, err_msg) = arg
        #        msg = "����������ʧ��: %s, errno=%d, ��رճ�������´�����" % (err_msg, errno)
        except:
            msg = "����������ʧ��, ��رճ�������´�����"
            self.infoText.SetValue(msg)
            #self.saveBtn.Enable(True)
        sock.close()


if __name__ == '__main__':  
    App().main()

