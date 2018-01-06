# imad_task3
group task

My language framework is backend Python-flask

* Python 2.6 or higher is usually required for installation for Flask on windows.
* The following command installs Virtual Environment
                * pip install virtualenv
* It will get installed in the path C:/pythonX/scripts path.Here X is the version name of Python. pip install virtualenv

 * Once installed, new virtual environment is created in a folder.

    * mkdir newproj
    * cd newproj
    * virtualenv venv

* To activate corresponding environment, on Linux/OS X, use the following − On Windows, following can be used −
     
     * venv\scripts\activate

* We are now ready to install Flask in this environment.

    * pip install Flask
#Steps to run python-flask files:


* Step1:Open Command Prompt and go to the directory where the file is located
    Eg:E:\python
    
* Step2:Type: python filename.py and Enter if you get the error stating that python is not recognized as internal or external command 
then
go to properties of 
This Pc--->Go to Advanced System Settings--->Go to Environmental variables--->Select Path and Edit-->Type ";" at the end 
  and 
copy the path of the python application and give ok.
Eg:C:\Users\sandya\AppData\Local\Programs\Python\Python36.

  * Incase,if you didn't get any error then the cmd prompt will display the following lines:
                         * Restarting with stat
                         * Debugger is active!
                         * Debugger PIN: 264-240-688
                         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
                         
                         
* Step3:Then go to the local host "http://127.0.0.1:5000/" in your browser. To see the output add the extensions specified in the code.

 #Step4:TO RUN app.py

1.app.py displays the list of customers,lists the subscription plan which is created manually.

  #Before running app.py follow the procedures which I mentioned
   * To run the app.py in windoes command prompt follow the steps,
                    * we should input the secret API KEY and publishable API KEY.
                    * command is "set your secret API KEY"(not within the double quotes)
                                  "set publishable API KEY"(not within the double quotes)
                    * After entering the api key type:python app.py
                    
                    
 
