# TO START USING THE PROJECT YOU HAVE TO DO SOME SETUPS:

# 1.1) Go to the ./necessaryData directory and complete all the steps specified in the README.txt file;

# 1.2) Replace "username" and "password" in the ./scripts/instagram/__init __.py file on your username and your password;
    
# 1.3) Paste instagram account links(links exactly, not usernames) that suppose to be reported into the ./scripts/generalUsedTools/linksOnEnemies/unparsedLinks file. There is already much text in the file, and the text was taken from the telegram group https://t.me/stoprussiachannel. 
# And that's exactly why file is named "unparsedLinks": you can paste there any text with links and the script will clearly parse all the links from the all other junk;

# *** After you have accomplished all these steps you can start running the project;

.

.

.

# What text files are responsible for:

# 1. unparsedLinks is the file with all the text/links you paste in.
# 2. allParsedLinks.txt is the file with all the links that have been collected from the unparsedLinks file. It's a file with just links, nothing more(no junk).
# 3. reportedOnesInst.txt is the file with all the instagram account that have been already reported.

.

# ALGORITHM STEPS OF HOW PROJECT WORKS you can see in the terminal output when you run the script.

.

.

# *** This project was supposed to be multi social media report application, not only for instagram, but for Twitter, YouTube, TikTok and Facebook as well. That's exactly why ./scripts folder is divided on "generalUsedTools" and "instagram" packages, there were supposed to be packages for the all other social medias. I just have no enough time to write automation scripts for them all.
