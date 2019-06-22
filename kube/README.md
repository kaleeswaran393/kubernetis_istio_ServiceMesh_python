# kubernatis_ingress_stickysession_Scaling

### Input Variables needed

target: backend1/ backend2/ backend3
username: <Any name>

### Running locally

This program takes two input from the user. You can either post the input using postman tool or using curl. Below is the step by step procedure for running this program.

1. Download all the files locally
2. Start the minikube locally and give the below commands
	`kubectl apply -f backend1.yaml`
    `kubectl apply -f backend2.yaml`
    `kubectl apply -f backend2.yaml`
    `kubectl apply -f backend-ingress.yaml`
    
3. Check the pods in your minikube using this command `kubectl get pods`. You can see there will be two pods for each backend running.
4. Get the minikube ip using the command `minikube ip`
5. Now open the postman and give the url as https://<minikubeip>:8080/hit_backend with header as "Content-Type: application/json" and input the body as `{"target":"backend-1", "username":"user1"}`
6. Using curl command:
	`curl -d '{"target":"backend-1", "username":"user one"}' -H "Content-Type: application/json" -X POST <minikubeid>:8080/hit_backend`
7. You will get the output as :
  `{'username': 'user1', 'target': 'backend-1', 'podIp': '192.168.1.128'}`
8. Try the input with different username and different target, check the podIP gives the same IP for the given user.
 
