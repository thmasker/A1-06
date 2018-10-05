# A1-06
Intelligent Systems Git repository

INSTRUCTIONS TO TEST Graph.py
	Running tests.py script, you can check both three methods created on src/Graph.py
	
IMPORTANT!!!
	Before pushing any new changes, you must do a "Downloading new changes" operation. You can only commit without doing it

INSTRUCTIONS TO USE Git

	FIRST USE
		1. git remote add upstream git@github.com:thmasker/A1-06.git

	-- Downloading new changes
		1. git fetch upstream
		2. git checkout master
		3. git merge upstream/master
			-- Update your personal fork after downloading new changes
				1. git push

	-- Uploading new changes to your personal fork
		1. git add file (or * if you want to add all files changed)
		2. git commit -m "message"
		3. git push
			-- Update the original branch after uploading new changes to your personal fork
				1. go to your personal fork on github.com and press Create pull request
