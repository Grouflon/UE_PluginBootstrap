import sys
import os
import fileinput

def replaceInFile(file, replacedText, replacementText):
    with fileinput.FileInput(file, inplace=True) as file:
        for line in file:
            print(line.replace(replacedText, replacementText), end='')

assert len(sys.argv) > 1, "Missing new plugin name argument"

oldPluginName = 'PluginBootstrap'
newPluginName = sys.argv[1]

print('Replacing text in files...')
replaceInFile('./PluginBootstrap.uplugin', oldPluginName, newPluginName)
replaceInFile('./Source/PluginBootstrapEditor/PluginBootstrapEditor.Build.cs', oldPluginName, newPluginName)
replaceInFile('./Source/PluginBootstrapEditor/PluginBootstrapEditorModule.cpp', oldPluginName, newPluginName)
replaceInFile('./Source/PluginBootstrapEditor/PluginBootstrapEditorModule.h', oldPluginName, newPluginName)
replaceInFile('./Source/PluginBootstrapRuntime/PluginBootstrapRuntime.Build.cs', oldPluginName, newPluginName)
replaceInFile('./Source/PluginBootstrapRuntime/PluginBootstrapRuntimeModule.cpp', oldPluginName, newPluginName)
replaceInFile('./Source/PluginBootstrapRuntime/PluginBootstrapRuntimeModule.h', oldPluginName, newPluginName)
print('Done\n')

print('Renaming files and folders...')
os.rename('./PluginBootstrap.uplugin', './{0}.uplugin'.format(newPluginName))
os.rename('./Source/PluginBootstrapEditor/PluginBootstrapEditor.Build.cs', './Source/PluginBootstrapEditor/{0}Editor.Build.cs'.format(newPluginName))
os.rename('./Source/PluginBootstrapEditor/PluginBootstrapEditorModule.cpp', './Source/PluginBootstrapEditor/{0}EditorModule.cpp'.format(newPluginName))
os.rename('./Source/PluginBootstrapEditor/PluginBootstrapEditorModule.h', './Source/PluginBootstrapEditor/{0}EditorModule.h'.format(newPluginName))
os.rename('./Source/PluginBootstrapEditor', './Source/{0}Editor'.format(newPluginName))
os.rename('./Source/PluginBootstrapRuntime/PluginBootstrapRuntime.Build.cs', './Source/PluginBootstrapRuntime/{0}Runtime.Build.cs'.format(newPluginName))
os.rename('./Source/PluginBootstrapRuntime/PluginBootstrapRuntimeModule.cpp', './Source/PluginBootstrapRuntime/{0}RuntimeModule.cpp'.format(newPluginName))
os.rename('./Source/PluginBootstrapRuntime/PluginBootstrapRuntimeModule.h', './Source/PluginBootstrapRuntime/{0}RuntimeModule.h'.format(newPluginName))
os.rename('./Source/PluginBootstrapRuntime', './Source/{0}Runtime'.format(newPluginName))
print('Done\n')
print('All Good')
