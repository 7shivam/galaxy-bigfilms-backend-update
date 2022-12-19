#Galaxy_BigFilms_Backend_python
1) Docker command to run container is
2) docker run -itd -p 8000:8000 -e IP_ADDRESS=localhost -e HOST_NAME=root -e HOST_PASS=root -e DATABASE=s3_moviemasala_db backend

# Deployment on Kubernetes Cluster 

1) Create kubernetes secret named "mysqlsecret" and define mysql-user, mysql-password and mysql-database in it. 
2) Create db using db.yaml file 

```bash 
kubectl apply -f db.yaml
```

3) Check status and start deploying backend once db is up 

```bash
kubectl apply -f backend.yaml
kubectl get pods
```
4) create db data after db and backend pod creation. Exec to db pod, login mysql using mysql username and password.

```bash
$ kubectl exec -it $DB_POD_NAME /bin/bash
$ mysql -u root -p $MYSQL_DATABASE #it will prompt for a password
$ INSERT INTO `movie`(
	`id` ,
	`Name` ,
	`Actors` ,
	`Release` ,
        `Rating`,
        `Image` 
)
VALUES(
	'1' ,
	'wanted' ,
	'Salman Khan' ,
        '2018-07-01' ,
        '5' ,
        'https://social-filmytadka-movies-images.s3.amazonaws.com/avengers.jpeg'
	
);
$ \q
$ exit
```

4) Now hit backend service url (http://backend-service-external-ip:8000) and check if inseted data visible.
5) Deploy frontend using [repo](https://github.com/tvc-ctg/galaxy-bigfilms-frontend/react-frontend/kubernetes/frontend.yaml)

```bash
$ kubectl apply -f frontend.yaml
```

6) You should see below entry after hitting the frontend Url 

![image](https://user-images.githubusercontent.com/36677428/188502955-9d4193e8-ed9f-435b-acb1-5820004f1eb6.png)



  
