Remove-Item build -Force -Recurse -ErrorAction SilentlyContinue
Remove-Item dist -Force -Recurse -ErrorAction SilentlyContinue
Get-ChildItem *.c -Recurse | foreach { Remove-Item -Path $_.FullName }
Get-ChildItem *.pyd -Recurse | foreach { Remove-Item -Path $_.FullName }
Remove-Item src\version.py -Force -Recurse -ErrorAction SilentlyContinue