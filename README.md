# Use Case : 
1. Three simple python backend-service (i.e: app1.py, app2.py, app3.py), all have the same endpoint /hit_backend, which receives a message over an HTTP REST endpoint (/hit_backend) and responds with the following output:
Input: {"target":"backend-1", "username":"user one"}
Output: {"service_name":"backend-1","username":"user one","pod_id":"1"}
 
2. These 3 back-end should be hosted on k8s setup within minikube/localhost (i.e: app1.py -> backend-1, app2.py -> backend-2, app3.py -> backend-3) and each back-end with a minimum of 3 and a maximum of 5 replicas for the above server process (auto-scaling).
 
3. A loadbalancer with k8s ingress and custom nginx/haproxy ingress controller that route /hit_backend traffic based on the following routing rules:
- Use "target" field in request body or request header to route to corresponding backend (i.e: "target":"backend-1" route to backend-1 service)
- sticky session: request with the same "username" should reach the same replicas if called within 1 minute from the previous one

## Key features :
	Json content based sticky session and routing
	Username based sticky session
	routing to backend based on the input field target
	the sticky session would expire in one minute
	Enabled Horizontal pod if resource utilization reaches 50%
	
## Steps

### 1. Steps to install istio in minikube
        https://doc.istio.cn/en/docs/setup/kubernetes/download-release/
	https://github.com/istio/istio/releases
	https://istio.io/docs/setup/kubernetes/install/kubernetes/ (Change gateway type as NodePort and install in demo.xml)
	https://istio.io/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports
	https://istio.io/docs/examples/bookinfo/
	
### 1. Backend Server - Python
	  
### 2. K8s Resources
	1. K8s Services are  Backend-1, backend-2, backend-3
	2. ReplicaSet for corresponging services
	3. Horizantal Auto Scaling for ReplicaSet
	
### 3 K8s - Istio Resources
	1. DestinationRule to maintain sticky session
	2. Virtual Service for Header based routing
	3. Istio Gateway
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
	target:backend-2
        Content-Type:application/json
        x-user:kaleeswaran
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
