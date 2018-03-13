# open-ebs-assesment
##First openebs Assesment

###Steps to Run the app
 1. Clone the repo
  ```git clone https://github.com/sandeep3119/open-ebs-assesment.git```
 2. cd to that folder
  ```cd open-ebs-assement```
 3. Apply the .yaml files to run the app.
  ```kubectl apply -f pods.yaml```
  ```kubectl apply -f deployment.yaml```
  ```kubectl apply -f service.yaml```
 4. Now run the docker command to give a manual user input to show on browser
  ```docker run -e user-name="<your-username>" -p 127.0.0.1:80:80 sandeep3119/test:v1```
 5. Open the link that was given as a output of step 4 and you can find your name there.

	

