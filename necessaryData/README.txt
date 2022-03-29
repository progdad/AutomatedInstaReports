
In this directory suppose to be saved:

    ************************
    1. Driver of Chrome browser:

        1.1) Open page https://chromedriver.chromium.org/downloads and find your chrome browser version:
            *** To find out your chrome browser version open chrome://version/
                and in the first row you'll see something like: Google Chrome	99.0.4844.51 (Official Build) (64-bit)
            99.0.4844.51 --- this is my version. there will be yours;

        1.2) Then click on your version and in the list of archives download archive for your operating system;
            *** For example for windows it will be named "chromedriver_win32.zip";

        1.3) After downloading, extract chromedriver(this is executable file) from archive
        and move it to the .\chromedriver\ directory;

            *** AT FIRST DELETE MY CHROMEDRIVER FROM THE DIRECTORY
    ************************

    ************************
    1. The path of your Chrome profile:

        1.1) Open again page chrome://version/ and find the path to your chrome profile:
            *** It is writen right from the variable "Profile Path";
                For example default path for Windows looks like:
                    Profile Path:   C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default;

        1.2) Copy the path and paste it to the .\chromeProfilePath\path file,
            but at first you have to remove the example path from the file;
    ************************
