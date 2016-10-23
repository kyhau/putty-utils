
regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham

cp "%userprofile%\Desktop\putty.reg" putty_dos2unix.reg

dos2unix putty_dos2unix.reg

virtualenv env
env\Scripts\activate

python putty_update_sessions_color_schema.py

# double click on putty_updated.reg to re-import