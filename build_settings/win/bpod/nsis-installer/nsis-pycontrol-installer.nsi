; Turn off old selected section
; 12 06 2005: Luis Wong
; Template voor het genereren van een installer.
; speciaal voor het genereren van EasyPlayer installers.
; Trimedia Interactive Projects


; -------------------------------
; Start


  !define MUI_PRODUCT "PyBpod-v1.3.1.beta"
  !define MUI_INPUT "C:\Users\swp_user\Desktop\bpod\PyBpodGUI_v1.3.1.beta_git63_build18.DEV\*"
  !define MUI_FILE "PyBpodGUI_v1.3.1.beta_git63_build18.DEV"
  !define MUI_VERSION "1.3.1.beta"
  !define MUI_BRANDINGTEXT "PyBpod Ver. 1.3.1.beta"
  CRCCheck On

  ; Bij deze moeten we waarschijnlijk een absoluut pad gaan gebruiken
  ; dit moet effe uitgetest worden.
  !include "${NSISDIR}\Contrib\Modern UI\System.nsh"


;---------------------------------
;General

  OutFile "pybpod-installer-v1.3.1.beta.exe"
  ShowInstDetails "nevershow"
  ShowUninstDetails "nevershow"
  ;SetCompressor "bzip2"

  !define MUI_ICON "cf_icon_128x128.ico"
  !define MUI_UNICON "cf_icon_128x128.ico"
  ;!define MUI_SPECIALBITMAP "Bitmap.bmp"


;--------------------------------
;Folder selection page

  InstallDir "$PROGRAMFILES\${MUI_PRODUCT}"


;--------------------------------
;Modern UI Configuration

  !define MUI_WELCOMEPAGE
  !define MUI_LICENSEPAGE
  !define MUI_DIRECTORYPAGE
  !define MUI_ABORTWARNING
  !define MUI_UNINSTALLER
  !define MUI_UNCONFIRMPAGE
  !define MUI_FINISHPAGE


;--------------------------------
;Language

  !insertmacro MUI_LANGUAGE "English"


;--------------------------------
;Modern UI System


!include "MUI.nsh"

!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES


;--------------------------------
;Data

  LicenseData "LICENSE"


;--------------------------------
;Installer Sections
Section "install" ;Installation info

;Add files
  SetOutPath "$INSTDIR"
  File /r "${MUI_INPUT}"


;create desktop shortcut
  CreateShortCut "$DESKTOP\${MUI_PRODUCT}.lnk" "$INSTDIR\${MUI_FILE}.exe" ""

;create start-menu items
  CreateDirectory "$SMPROGRAMS\${MUI_PRODUCT}"
  CreateShortCut "$SMPROGRAMS\${MUI_PRODUCT}\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\${MUI_PRODUCT}\${MUI_PRODUCT}.lnk" "$INSTDIR\${MUI_FILE}.exe" "" "$INSTDIR\${MUI_FILE}.exe" 0

;write uninstall information to the registry
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "DisplayName" "${MUI_PRODUCT} (remove only)"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "UninstallString" "$INSTDIR\Uninstall.exe"

  WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd


;--------------------------------
;Uninstaller Section
Section "Uninstall"

;Delete Files
  RMDir /r "$INSTDIR\*.*"

;Remove the installation directory
  RMDir "$INSTDIR"

;Delete Start Menu Shortcuts
  Delete "$DESKTOP\${MUI_PRODUCT}.lnk"
  Delete "$SMPROGRAMS\${MUI_PRODUCT}\*.*"
  RmDir  "$SMPROGRAMS\${MUI_PRODUCT}"

;Delete Uninstaller And Unistall Registry Entries
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\${MUI_PRODUCT}"
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}"

SectionEnd


;--------------------------------
;MessageBox Section


;Function that calls a messagebox when installation finished correctly
Function .onInstSuccess
  MessageBox MB_OK "You have successfully installed ${MUI_PRODUCT}. Use the desktop icon to start the program."
FunctionEnd


Function un.onUninstSuccess
  MessageBox MB_OK "You have successfully uninstalled ${MUI_PRODUCT}."
FunctionEnd


;eof