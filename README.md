# initial-setup
- translusant TB
- ARC Browser
- Docker
- Cursor
- Vscode
- insomnia

# Keyword Bindings 
```
[
  {
    "key": "shift+enter",
    "command": "python.execInTerminal-icon"
  },
  {
    "key": "ctrl+enter",
    "command": "notebook.cell.executeAndInsertBelow",
    "when": "notebookCellListFocused && notebookCellType == 'markup' || notebookCellListFocused && notebookMissingKernelExtension && !notebookCellExecuting && notebookCellType == 'code' || notebookCellListFocused && !notebookCellExecuting && notebookCellType == 'code' && notebookKernelCount > 0 || notebookCellListFocused && !notebookCellExecuting && notebookCellType == 'code' && notebookKernelSourceCount > 0"
  },
  {
    "key": "ctrl+'",
    "command": "workbench.action.terminal.new",
    "when": "terminalProcessSupported || terminalWebExtensionContributedProfile"
  },
  {
    "key": "ctrl+shift+`",
    "command": "-workbench.action.terminal.new",
    "when": "terminalProcessSupported || terminalWebExtensionContributedProfile"
  },
  
]
```
