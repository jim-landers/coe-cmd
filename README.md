# coecmd

A command line tool which enables quick navigation to various webpages and internal tools used by the COE IT department. I started this project for myself because I got tired of constantly clicking through bookmarks and searchbars while working on tickets.

Anyone can feel free to suggest additional features or contribute to this project if you think of anything which should be added.

Special thanks to [@cdgco](https://github.com/cdgco) for creating the COETools API as a solution for JitBit's API not supporting some important basic features.

# Setup Guide
This tool is tailored to only work on COE domain machines. This setup process should not require any admin permissions at any point.

1. Have a working version of Python3 on your machine. (Available in Software Center)
2. Clone/Download this project to your network Home Directory. This means the project's filepath should look something like: *"Z:\coecmd"* or *"\\\depot.engr.oregonstate.edu\Users\YourONID\coecmd"*.
3. Run `setup.bat` in the project folder.
4. Restart any open terminal windows.
5. Run the command `coecmd`. If it runs and prints a list of currently supported commands, the setup was successful.

**IMPORTANT NOTE:** The `setup.bat` currently overwrites any directories you have custom added to your profile's Windows PATH. If this is a concern, it should be fairly simple to just delete the `setx` line from the `setup.bat`, then add *"~\\.local\bin"* to your profile's PATH manually. (This shouldn't be a problem for most people.)



