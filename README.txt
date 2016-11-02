------------------------
allegro-scrap_selenium
------------------------

The requriment:

I want it go on site allegro.pl/myaccount (take login:password from login.txt file, post login) ---> login correct --> go to Step2 ; login incorrect --> take new account:password from login.txt and try again.

Step2. Go to http://allegro.pl/myaccount/cards.php and check if certain phrase (3 words) exist on page - if exists, pause working, save login:password of account used (data from login.txt), to result.txt file on shell and while being paused debug me information on shell if I want to (C)ontinue with new account or (S)top operation /// if phrase doesnt exist, delete cookies and take new account.

Step3. After I submit (C)ontinue, delete cookies and go to Step1 with next account from login.txt and go further.

I can supply you account on that site, or you can register account there yourself so you can see whats inside.


Instructions of use:

1. Install the requeriments file

	pip install -r requeriments

2. Install the firefox version inside the file

3. Check the route to the login and results directories inside 
the python file , make sure the structure

4. Execute the python file

	python allegro-scrap_selenium.py
