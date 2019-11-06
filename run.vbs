set ws = createobject("wscript.shell")
ws.CurrentDirectory =  createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
ws.run "cmd /c python.exe sel.py",0