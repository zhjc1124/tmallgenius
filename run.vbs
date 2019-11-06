set ws = createobject("wscript.shell")
ws.CurrentDirectory =  createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
ws.run "cmd /c python.exe pybilibili.py",0