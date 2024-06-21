# autoupdategit - your helper in server managment!
Automatically update your repository on server (Ubuntu) every day.

Now you can autoupdate your scripts on server without any activities on your side!

❗IMPORTANT❗ 
Rename "yournamescript" in the code to name your repo (example -> autoupdategit)

❓ How to use it?

Use this steps:
* Download the main file (autoupdate.py) and place it in the directory of your repository.
* Run the file by executing the command "python autoupdate.py".
* To test the functionality, you can use the "forceupdate" command. This command updates your repository without any wait time.
* Your repository will update at 00:00 local time every day.

🛠️ Commands:

forceupdate - update your repo without waiting
countdown - time until next update from git.

📃 Note:

If the script cannot find your repository, it will clone it to the folder containing the autoupdate script.
