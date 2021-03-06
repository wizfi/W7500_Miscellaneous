# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class W7500_ISP
###########################################################################

class W7500_ISP ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"W7500 ISP Tool", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( 9, 74, 90, 90, False, "Verdana" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer_Step1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 1 - Serial Option" ), wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText_serial_port = wx.StaticText( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_serial_port.Wrap( -1 )
		fgSizer4.Add( self.m_staticText_serial_port, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_comboBox_serial_portChoices = []
		self.m_comboBox_serial_port = wx.ComboBox( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_serial_portChoices, 0 )
		fgSizer4.Add( self.m_comboBox_serial_port, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button_serial_refresh = wx.Button( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button_serial_refresh, 0, wx.ALL, 5 )
		
		self.m_staticText_baud_rate = wx.StaticText( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, u"Baud Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_baud_rate.Wrap( -1 )
		fgSizer4.Add( self.m_staticText_baud_rate, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		m_comboBox_baud_rateChoices = [ u"2400", u"9600", u"14400", u"19200", u"38400", u"57600", u"76800", u"115200", u"230400", u"460800" ]
		self.m_comboBox_baud_rate = wx.ComboBox( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_baud_rateChoices, 0 )
		self.m_comboBox_baud_rate.SetSelection( 7 )
		fgSizer4.Add( self.m_comboBox_baud_rate, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button_serial_open = wx.Button( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_serial_open.SetDefault() 
		fgSizer4.Add( self.m_button_serial_open, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button_serial_close = wx.Button( sbSizer_Step1.GetStaticBox(), wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_serial_close.SetDefault() 
		self.m_button_serial_close.Enable( False )
		
		fgSizer4.Add( self.m_button_serial_close, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer_Step1.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		gbSizer1.Add( sbSizer_Step1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer_Step2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 2 - Erase" ), wx.VERTICAL )
		
		bSizer_Step2_Child = wx.BoxSizer( wx.VERTICAL )
		
		m_listBox_EraseBlockChoices = [ u"Erase Data  0 (0x0003FE00~0x0003FEFF)", u"Erase Data  1 (0x0003FF00~0x0003FFFF)", u"Erase Block 0 (0x00000000~0x00000FFF)", u"Erase Block 1 (0x00001000~0x00001FFF)", u"Erase Block 2 (0x00002000~0x00002FFF)", u"Erase Block 3 (0x00003000~0x00003FFF)", u"Erase Block 4 (0x00004000~0x00004FFF)", u"Erase Block 5 (0x00005000~0x00005FFF)", u"Erase Block 6 (0x00006000~0x00006FFF)", u"Erase Block 7 (0x00007000~0x00007FFF)", u"Erase Block 8 (0x00008000~0x00008FFF)", u"Erase Block 9 (0x00009000~0x00009FFF)", u"Erase Block10 (0x0000A000~0x0000AFFF)", u"Erase Block11 (0x0000B000~0x0000BFFF)", u"Erase Block12 (0x0000C000~0x0000CFFF)", u"Erase Block13 (0x0000D000~0x0000DFFF)", u"Erase Block14 (0x0000E000~0x0000EFFF)", u"Erase Block15 (0x0000F000~0x0000FFFF)", u"Erase Block16 (0x00010000~0x00010FFF)", u"Erase Block17 (0x00011000~0x00011FFF)", u"Erase Block18 (0x00012000~0x00012FFF)", u"Erase Block19 (0x00013000~0x00013FFF)", u"Erase Block20 (0x00014000~0x00014FFF)", u"Erase Block21 (0x00015000~0x00015FFF)", u"Erase Block22 (0x00016000~0x00016FFF)", u"Erase Block23 (0x00017000~0x00017FFF)", u"Erase Block24 (0x00018000~0x00018FFF)", u"Erase Block25 (0x00019000~0x00019FFF)", u"Erase Block26 (0x0001A000~0x0001AFFF)", u"Erase Block27 (0x0001B000~0x0001BFFF)", u"Erase Block28 (0x0001C000~0x0001CFFF)", u"Erase Block29 (0x0001D000~0x0001DFFF)", u"Erase Block30 (0x0001E000~0x0001EFFF)", u"Erase Block31 (0x0001F000~0x0001FFFF)" ]
		self.m_listBox_EraseBlock = wx.ListBox( sbSizer_Step2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_EraseBlockChoices, wx.LB_MULTIPLE )
		self.m_listBox_EraseBlock.Enable( False )
		self.m_listBox_EraseBlock.SetMinSize( wx.Size( 100,70 ) )
		
		bSizer_Step2_Child.Add( self.m_listBox_EraseBlock, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_checkBox_erase_mass = wx.CheckBox( sbSizer_Step2.GetStaticBox(), wx.ID_ANY, u"Erase Data Block All Code Block", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_erase_mass.SetValue(True) 
		bSizer_Step2_Child.Add( self.m_checkBox_erase_mass, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_checkBox_erase_chip = wx.CheckBox( sbSizer_Step2.GetStaticBox(), wx.ID_ANY, u"Erase All Code Block", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Step2_Child.Add( self.m_checkBox_erase_chip, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer_Step2.Add( bSizer_Step2_Child, 0, wx.EXPAND, 5 )
		
		
		gbSizer1.Add( sbSizer_Step2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer_Step3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 3 - Code Read Lock or Data R/W Lock" ), wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox_all_code_read_lock = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"All Code Read Lock/Data R/W Lock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox_all_code_read_lock, 0, wx.ALL, 5 )
		
		self.m_checkBox_all_code_read_unlock = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"All Code Read Unlock/Data R/W Unlock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox_all_code_read_unlock, 0, wx.ALL, 5 )
		
		
		sbSizer_Step3.Add( bSizer9, 0, wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox_crl = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"Code Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_crl, 0, wx.ALL, 5 )
		
		self.m_checkBox_cabwl = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"Code All Block Write", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_cabwl, 0, wx.ALL, 5 )
		
		
		sbSizer_Step3.Add( bSizer10, 0, wx.ALL, 5 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox_drl1 = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"Data 1 Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_checkBox_drl1, 0, wx.ALL, 5 )
		
		self.m_checkBox_drl0 = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"Data 0 Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_checkBox_drl0, 0, wx.ALL, 5 )
		
		
		sbSizer_Step3.Add( bSizer101, 0, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox_dwl1 = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"Data 1 Write", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_checkBox_dwl1, 0, wx.ALL, 5 )
		
		self.m_checkBox_dwl0 = wx.CheckBox( sbSizer_Step3.GetStaticBox(), wx.ID_ANY, u"Data 0 Write", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_checkBox_dwl0, 0, wx.ALL, 5 )
		
		
		sbSizer_Step3.Add( bSizer111, 0, wx.EXPAND, 5 )
		
		
		gbSizer1.Add( sbSizer_Step3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		bSizer5.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		bSizer921 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer921.SetMinSize( wx.Size( 850,20 ) ) 
		
		bSizer921.AddSpacer( ( 0, 0), 1, wx.EXPAND, 100 )
		
		
		bSizer5.Add( bSizer921, 0, 0, 5 )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer_Step4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 4 - Code Write Lock" ), wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox_all_code_write_lock = wx.CheckBox( sbSizer_Step4.GetStaticBox(), wx.ID_ANY, u"All Code Write Lock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox_all_code_write_lock, 0, wx.ALL, 5 )
		
		self.m_checkBox_all_code_write_unlock = wx.CheckBox( sbSizer_Step4.GetStaticBox(), wx.ID_ANY, u"All Code Write Unlock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox_all_code_write_unlock, 0, wx.ALL, 5 )
		
		
		sbSizer_Step4.Add( bSizer11, 0, wx.EXPAND|wx.ALL, 5 )
		
		sbSizer_code_write_block = wx.StaticBoxSizer( wx.StaticBox( sbSizer_Step4.GetStaticBox(), wx.ID_ANY, u"Block" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 0, 16, 0, 0 )
		
		self.m_staticText_cwl31 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"31", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl31.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText_cwl30 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl30.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText_cwl29 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"29", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl29.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl28 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"28", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl28.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl27 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"27", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl27.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl26 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"26", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl26.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl25 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl25.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl24 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl24.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl23 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl23.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl22 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl22.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl21 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl21.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl20 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl20.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl19 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl19.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl18 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl18.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl17 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl17.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl16 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl16.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl31 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl30 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl29 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl28 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl27 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl26 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl25 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl24 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl23 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl22 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl21 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl20 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl19 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl18 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl17 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl16 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl15 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl15.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl14 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl14.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl13 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl13.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl12 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl12.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl11 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl11.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl10 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl10.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl9 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl9.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl8 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl8.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl7 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl7.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl6 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl6.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl5 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl5.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl4 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl4.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl3 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl3.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl2 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl2.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl1 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl1.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_cwl0 = wx.StaticText( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cwl0.Wrap( -1 )
		gSizer8.Add( self.m_staticText_cwl0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl15 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl14 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl13 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl12 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl11 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl10 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl9 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl8 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl7 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl6 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl5 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl4 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl3 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl2 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl1 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox_cwl0 = wx.CheckBox( sbSizer_code_write_block.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_checkBox_cwl0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer_code_write_block.Add( gSizer8, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		
		sbSizer_Step4.Add( sbSizer_code_write_block, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		gbSizer2.Add( sbSizer_Step4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer_Step5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 5 - Select the binary file" ), wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_Binary_File = wx.StaticText( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, u"Binary File :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Binary_File.Wrap( -1 )
		fgSizer5.Add( self.m_staticText_Binary_File, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_File_Path = wx.TextCtrl( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl_File_Path, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button_browse = wx.Button( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button_browse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer14.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		sbSizer_Step5.Add( bSizer14, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox_verify = wx.CheckBox( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, u"Verify after programming", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_verify.Enable( False )
		
		bSizer15.Add( self.m_checkBox_verify, 0, wx.ALL, 5 )
		
		self.m_checkBox_WriteMainFlash = wx.CheckBox( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, u"Write MainFlash", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_WriteMainFlash.SetValue(True) 
		bSizer15.Add( self.m_checkBox_WriteMainFlash, 0, wx.ALL, 5 )
		
		self.m_checkBox_WriteDataFlash = wx.CheckBox( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, u"Write DataFlash", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBox_WriteDataFlash, 0, wx.ALL, 5 )
		
		
		sbSizer_Step5.Add( bSizer15, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button_Isp_start = wx.Button( sbSizer_Step5.GetStaticBox(), wx.ID_ANY, u"ISP Start", wx.DefaultPosition, wx.Size( 300,30 ), 0 )
		self.m_button_Isp_start.SetFont( wx.Font( 12, 74, 90, 92, False, "Verdana" ) )
		
		bSizer91.Add( self.m_button_Isp_start, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer_Step5.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		gbSizer2.Add( sbSizer_Step5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		bSizer5.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		bSizer92 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer92.SetMinSize( wx.Size( 850,20 ) ) 
		
		bSizer92.AddSpacer( ( 0, 0), 1, wx.EXPAND, 100 )
		
		
		bSizer5.Add( bSizer92, 0, 0, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		bSizer5.Fit( self )
		self.m_statusBar_W7500_Status = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menu_file.AppendSeparator()
		
		self.m_menu2 = wx.Menu()
		self.m_menu_file.AppendSubMenu( self.m_menu2, u"&Quit\tCtrl+Q" )
		
		self.m_menubar1.Append( self.m_menu_file, u"&File" ) 
		
		self.m_menu_ISP = wx.Menu()
		self.m_menuItem_HexEditor = wx.MenuItem( self.m_menu_ISP, wx.ID_ANY, u"&HexEditor", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_ISP.AppendItem( self.m_menuItem_HexEditor )
		
		self.m_menu_Dump = wx.Menu()
		self.m_menuItem_MainFlashDump = wx.MenuItem( self.m_menu_Dump, wx.ID_ANY, u"&Main Flash Dump", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_Dump.AppendItem( self.m_menuItem_MainFlashDump )
		
		self.m_menuItem_Data_Dump = wx.MenuItem( self.m_menu_Dump, wx.ID_ANY, u"&Data Dump ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_Dump.AppendItem( self.m_menuItem_Data_Dump )
		
		self.m_menu_ISP.AppendSubMenu( self.m_menu_Dump, u"&Dump" )
		
		self.m_menubar1.Append( self.m_menu_ISP, u"&ISP" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menubar1.Append( self.m_menu_help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.VERTICAL )
		
		# Connect Events
		self.m_button_serial_refresh.Bind( wx.EVT_BUTTON, self.onRefresh )
		self.m_button_serial_open.Bind( wx.EVT_BUTTON, self.onSerialOpen )
		self.m_button_serial_close.Bind( wx.EVT_BUTTON, self.onSerialClose )
		self.m_checkBox_erase_mass.Bind( wx.EVT_CHECKBOX, self.onCheckEraseMass )
		self.m_checkBox_erase_chip.Bind( wx.EVT_CHECKBOX, self.onCheckEraseChip )
		self.m_checkBox_all_code_read_lock.Bind( wx.EVT_CHECKBOX, self.onAllCodeReadLock )
		self.m_checkBox_all_code_read_unlock.Bind( wx.EVT_CHECKBOX, self.onAllCodeReadUnlock )
		self.m_checkBox_all_code_write_lock.Bind( wx.EVT_CHECKBOX, self.onAllCodeWriteLock )
		self.m_checkBox_all_code_write_unlock.Bind( wx.EVT_CHECKBOX, self.onAllCodeWriteUnlock )
		self.m_button_browse.Bind( wx.EVT_BUTTON, self.onBrowse )
		self.m_checkBox_WriteMainFlash.Bind( wx.EVT_CHECKBOX, self.onWriteMainFlash )
		self.m_checkBox_WriteDataFlash.Bind( wx.EVT_CHECKBOX, self.onWriteDataFlash )
		self.m_button_Isp_start.Bind( wx.EVT_BUTTON, self.onISP_Start )
		self.Bind( wx.EVT_MENU, self.onHexEditor, id = self.m_menuItem_HexEditor.GetId() )
		self.Bind( wx.EVT_MENU, self.onFlashDump, id = self.m_menuItem_MainFlashDump.GetId() )
		self.Bind( wx.EVT_MENU, self.onDataDump, id = self.m_menuItem_Data_Dump.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onRefresh( self, event ):
		event.Skip()
	
	def onSerialOpen( self, event ):
		event.Skip()
	
	def onSerialClose( self, event ):
		event.Skip()
	
	def onCheckEraseMass( self, event ):
		event.Skip()
	
	def onCheckEraseChip( self, event ):
		event.Skip()
	
	def onAllCodeReadLock( self, event ):
		event.Skip()
	
	def onAllCodeReadUnlock( self, event ):
		event.Skip()
	
	def onAllCodeWriteLock( self, event ):
		event.Skip()
	
	def onAllCodeWriteUnlock( self, event ):
		event.Skip()
	
	def onBrowse( self, event ):
		event.Skip()
	
	def onWriteMainFlash( self, event ):
		event.Skip()
	
	def onWriteDataFlash( self, event ):
		event.Skip()
	
	def onISP_Start( self, event ):
		event.Skip()
	
	def onHexEditor( self, event ):
		event.Skip()
	
	def onFlashDump( self, event ):
		event.Skip()
	
	def onDataDump( self, event ):
		event.Skip()
	

