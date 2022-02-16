Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import mydir
>>> help(mydir)
Help on module mydir:

NAME
    mydir

FUNCTIONS
    listing(module, verbose=True)

DATA
    sepchr = '-'
    seplen = 60

FILE
    c:\python\mydir.py


>>> mydir.py
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mydir.py
AttributeError: module 'mydir' has no attribute 'py'
>>> 
>>> mydir
<module 'mydir' from 'C:\\Python\\mydir.py'>
>>> print(mydir.py)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(mydir.py)
AttributeError: module 'mydir' has no attribute 'py'
>>> print(mydir)
<module 'mydir' from 'C:\\Python\\mydir.py'>
>>> import tkinter
>>> mydir.listing(tkinter)
------------------------------------------------------------
name: tkinter file: C:\Python\lib\tkinter\__init__.py
------------------------------------------------------------
00 __name__<built-in name>
01 __doc__<built-in name>
02 __package__<built-in name>
03 __loader__<built-in name>
04 __spec__<built-in name>
05 __path__<built-in name>
06 __file__<built-in name>
07 __cached__<built-in name>
08 __builtins__<built-in name>
09 enum<module 'enum' from 'C:\\Python\\lib\\enum.py'>
10 sys<module 'sys' (built-in)>
11 _tkinter<module '_tkinter' from 'C:\\Python\\DLLs\\_tkinter.pyd'>
12 TclError<class '_tkinter.TclError'>
13 constants<module 'tkinter.constants' from 'C:\\Python\\lib\\tkinter\\constants.py'>
14 NO0
15 FALSE0
16 OFF0
17 YES1
18 TRUE1
19 ON1
20 Nn
21 Ss
22 Ww
23 Ee
24 NWnw
25 SWsw
26 NEne
27 SEse
28 NSns
29 EWew
30 NSEWnsew
31 CENTERcenter
32 NONEnone
33 Xx
34 Yy
35 BOTHboth
36 LEFTleft
37 TOPtop
38 RIGHTright
39 BOTTOMbottom
40 RAISEDraised
41 SUNKENsunken
42 FLATflat
43 RIDGEridge
44 GROOVEgroove
45 SOLIDsolid
46 HORIZONTALhorizontal
47 VERTICALvertical
48 NUMERICnumeric
49 CHARchar
50 WORDword
51 BASELINEbaseline
52 INSIDEinside
53 OUTSIDEoutside
54 SELsel
55 SEL_FIRSTsel.first
56 SEL_LASTsel.last
57 ENDend
58 INSERTinsert
59 CURRENTcurrent
60 ANCHORanchor
61 ALLall
62 NORMALnormal
63 DISABLEDdisabled
64 ACTIVEactive
65 HIDDENhidden
66 CASCADEcascade
67 CHECKBUTTONcheckbutton
68 COMMANDcommand
69 RADIOBUTTONradiobutton
70 SEPARATORseparator
71 SINGLEsingle
72 BROWSEbrowse
73 MULTIPLEmultiple
74 EXTENDEDextended
75 DOTBOXdotbox
76 UNDERLINEunderline
77 PIESLICEpieslice
78 CHORDchord
79 ARCarc
80 FIRSTfirst
81 LASTlast
82 BUTTbutt
83 PROJECTINGprojecting
84 ROUNDround
85 BEVELbevel
86 MITERmiter
87 MOVETOmoveto
88 SCROLLscroll
89 UNITSunits
90 PAGESpages
91 re<module 're' from 'C:\\Python\\lib\\re.py'>
92 wantobjects1
93 TkVersion8.6
94 TclVersion8.6
95 READABLE2
96 WRITABLE4
97 EXCEPTION8
98 _magic_rere.compile('([\\\\{}])')
99 _space_rere.compile('([\\s])', re.ASCII)
100 _join<function _join at 0x0000000002A58E18>
101 _stringify<function _stringify at 0x0000000002A8BA60>
102 _flatten<built-in function _flatten>
103 _cnfmerge<function _cnfmerge at 0x0000000002A8BAE8>
104 _splitdict<function _splitdict at 0x0000000002A8BB70>
105 EventType<enum 'EventType'>
106 Event<class 'tkinter.Event'>
107 _support_default_root1
108 _default_rootNone
109 NoDefaultRoot<function NoDefaultRoot at 0x0000000002A8BBF8>
110 _tkerror<function _tkerror at 0x0000000002A8BE18>
111 _exit<function _exit at 0x0000000002A8BEA0>
112 _varnum0
113 Variable<class 'tkinter.Variable'>
114 StringVar<class 'tkinter.StringVar'>
115 IntVar<class 'tkinter.IntVar'>
116 DoubleVar<class 'tkinter.DoubleVar'>
117 BooleanVar<class 'tkinter.BooleanVar'>
118 mainloop<function mainloop at 0x0000000002A8BF28>
119 getint<class 'int'>
120 getdouble<class 'float'>
121 getboolean<function getboolean at 0x0000000002AD4BF8>
122 Misc<class 'tkinter.Misc'>
123 CallWrapper<class 'tkinter.CallWrapper'>
124 XView<class 'tkinter.XView'>
125 YView<class 'tkinter.YView'>
126 Wm<class 'tkinter.Wm'>
127 Tk<class 'tkinter.Tk'>
128 Tcl<function Tcl at 0x0000000002AD4C80>
129 Pack<class 'tkinter.Pack'>
130 Place<class 'tkinter.Place'>
131 Grid<class 'tkinter.Grid'>
132 BaseWidget<class 'tkinter.BaseWidget'>
133 Widget<class 'tkinter.Widget'>
134 Toplevel<class 'tkinter.Toplevel'>
135 Button<class 'tkinter.Button'>
136 Canvas<class 'tkinter.Canvas'>
137 Checkbutton<class 'tkinter.Checkbutton'>
138 Entry<class 'tkinter.Entry'>
139 Frame<class 'tkinter.Frame'>
140 Label<class 'tkinter.Label'>
141 Listbox<class 'tkinter.Listbox'>
142 Menu<class 'tkinter.Menu'>
143 Menubutton<class 'tkinter.Menubutton'>
144 Message<class 'tkinter.Message'>
145 Radiobutton<class 'tkinter.Radiobutton'>
146 Scale<class 'tkinter.Scale'>
147 Scrollbar<class 'tkinter.Scrollbar'>
148 Text<class 'tkinter.Text'>
149 _setit<class 'tkinter._setit'>
150 OptionMenu<class 'tkinter.OptionMenu'>
151 Image<class 'tkinter.Image'>
152 PhotoImage<class 'tkinter.PhotoImage'>
153 BitmapImage<class 'tkinter.BitmapImage'>
154 image_names<function image_names at 0x0000000002ADE7B8>
155 image_types<function image_types at 0x0000000002AF1A60>
156 Spinbox<class 'tkinter.Spinbox'>
157 LabelFrame<class 'tkinter.LabelFrame'>
158 PanedWindow<class 'tkinter.PanedWindow'>
159 _test<function _test at 0x0000000002AF1AE8>
------------------------------------------------------------
tkinter has 160 names
------------------------------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> modname = "string"
>>> exec("import " + modname)
>>> string
<module 'string' from 'C:\\Python\\lib\\string.py'>
>>> 
>>> from reloadall import reload_all
>>> import as, tkinter
SyntaxError: invalid syntax
>>> import os, tkinter
>>> reload_all(os)
reloadingos
reloadingabc
reloadingsys
reloadingstat
reloadingntpath
reloadinggenericpath
>>> reload_all(tkinter)
reloadingtkinter
reloadingenum
reloadingsys
reloading_tkinter
reloadingtkinter.constants
reloadingre
reloadingsre_compile
reloading_sre
reloadingsre_parse
reloadingfunctools
reloading_locale
reloadingcopyreg
>>> 
>>> reload_all(os)
reloadingos
reloadingabc
reloadingsys
reloadingstat
reloadingntpath
reloadinggenericpath
>>> 
>>> reload_all(tkinter)
reloadingtkinter
reloadingenum
reloadingsys
reloading_tkinter
reloadingtkinter.constants
reloadingre
reloadingsre_compile
reloading_sre
reloadingsre_parse
reloadingfunctools
reloading_locale
reloadingcopyreg
>>> 
>>> import a
>>> a.X, a.b.Y, a.b.c.Z
(1, 2, 3)
>>> 
>>> reload(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    reload(a)
NameError: name 'reload' is not defined
>>> import reload
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    import reload
ModuleNotFoundError: No module named 'reload'
>>> from imp import reload
>>> 
>>> reload(a)
<module 'a' from 'C:\\Python\\a.py'>
>>> a.X, a.b.Y, a.b.c.Z
(111, 2, 3)
>>> 
>>> from reloadall import reload_all
>>> reload_all(a)
reloadinga
reloadingb
reloadingc
>>> a.X, a.b.Y, a.b.c.Z
(111, 222, 333)
>>> 
