CAPTCHA DETECTION

to use UI:
+ install nodejs
+ install npm
then cd to UI folder and run:
+ npm install (to build)
+ npm run serve (to start server)

on Browser install CORS Access-Control-Allow-Origin extension and turn it on
(UI server run best on Firefox)

to use python server: 
+ install python3, tensorflow and other requirement at file requirement.txt by command: pip install -r requirement.txt
+ follow other instructions to use tensorflow model at https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/?fbclid=IwAR0zqZzBY8BZ_cGWD-guWtBlbZOEZer9jGmuODaHFnzM54G7PxqroDtLO8o
+ to start server: cd to captcha_Server/research/object_detection/detect_captcha: python app.py

(need to start both servers to run this application successfully)