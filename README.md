# LoanApp
A loan app

---

- Server side, classic Django setup. My advice is to use a virtual env.

  In the root of the repo ( LoanApp ) do this:

  - `virtualenv loan_env`
  - `source loan_env/bin/activate`
  - `pip install -r requirements.txt`
  - `python manage.py makemigrations loan_app`
  - `python manage.py migrate`
  
  This should set up the project

- The frontend, used to demonstrate the token auth, can be served directly, since
  the bundle is checked in ( It's a simple react app )
  
  Run python `-m SimpleHTTPServer 8080` in the frotnend directory

  To rebuild the bundle, run yarn install in the frontend directory, followed by 
  `node_modules/webpack/bin/webpack.js`
   
  After the bundle is build, server with `python -m SimpleHTTPServer 8080`
   
- Logging can be seen by doing

  `tail -f /tmp/api_log.log`