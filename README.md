# kubernatis_istio_stickysession_Scaling

## Key features :
	Json content based sticky session and routing
	Username based sticky session
	routing to backend based on the input field target
	the sticky session would expire in one minute
	Enabled Horizontal pod if resource utilization reaches 50%
## Steps
### 1. Backend Server - Java
	   1. Endpoints are  - hit_backend, backend1, backend2, backend3 
### 2. K8s Objects
	1. K8s Services are  - Route-Service, Backend-1, backend-2, backend-3
	2. ReplicaSet for corresponging services
	3. Horizantal Auto Scaling for ReplicaSet
### 3. Build Java Project Using Maven
### 4. Dockerfile
	 1.docker build -t kubia:1.0.0 .
	 2.docker tag kubia:1.0.0  kaleeswarankaruppusamy/e2esystem:kubia4
	 3.docker push  <DOCKER_REPO>:kubia4
### 5. K8S Deployment Files
	  1. kubectl apply -f route-service.yaml
	  2. kubectl apply -f backend-ingress.yaml
	  3. kubectl apply -f backend-1.yaml
	  4. kubectl apply -f backend-2.yaml
	  5. kubectl apply -f backend-3.yaml
### 6.Sample Request and Reponse
	POST /hit_backend HTTP/1.1
	Host: localhost:8080
	Content-Type: application/json
	{
		"username": "user",
		"target":"backend-1"
	}

	Response : 
	{
	    "target": "backend-1",
	    "username": "user",
	    "podId": "backend-1-zlxtc"
	}
### Useful docker command
	Docker image prune --force
	docker image ls
	docker image rm
	docker load & Save
	docker ps -a 
	docker stop <containerid>
	docker rm 
### K8S Command
	1. brew cask install minikube   #install using virtualbox
	2. minikube status
	3. minikube delete
	4. minikube ip
	5. kubectl describe ing backend-ingress
	6. minikube dashboard   - K8s ui
	7. kubectl describe service servicename
	8. kubectl delete service servicename
	9. kubctl delete deployment deploymentname
	10 kubectl delete pod podname
	11. kubectl get service
	12. kubectl get pod
	13. kubectl get deplopyment
	14. kubectl get ReplicaSet
