@echo off
echo unfolding %* to .\@unfold
mkdir @unfold
for %%i in (%*) do (
	echo unfolding %%i to .\@unfold
	rem xcopy /s/e %%i\* .\@unfold
	robocopy %%i .\@unfold /E /J /NJH /NJS
	)
pause
