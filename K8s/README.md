
## Important terms for NetBackup deployment on EKS cluster

| Term | Description | Remarks |  
| -- | -- | -- |
Pod	 |A Pod is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. For more information on Pods, [see Kubernetes Documentation](https://kubernetes.io/docs/concepts/workloads/pods/).| |	
StatefulSet	| StatefulSet is the workload API object used to manage stateful applications and it represents a set of Pods with unique, persistent identities, and stable hostnames. For more information on StatefulSets, [see Kubernetes Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). | |	
Job	| Kubernetes jobs ensure that one or more pods execute their commands and exit successfully. For more information on Jobs, [see Kubernetes Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/job/). | | 	
ConfigMap |	A ConfigMap is an API object used to store non-confidential data in key-value pairs. For more information on ConfigMaps, https://kubernetes.io/docs/concepts/configuration/configmap/.	| |
Service |	A Service enables network access to a set of Pods in Kubernetes. For more information on Service, [see Kubernetes Documentation](https://kubernetes.io/docs/concepts/services-networking/service/). | | 	
PersistentVolume |	A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using storage classes. For more information on Persistent Volumes,[ see Kubernetes Documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).	| |
Custom Resource |	A Custom Resource (CR) is an extension of the Kubernetes API that is not necessarily available in a default Kubernetes installation. For more information on Custom Resources, [see Kubernetes Documentation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).	| |
Secret | A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in a container image. For more information on Secrets, [see Kubernetes Documentation.](https://kubernetes.io/docs/concepts/configuration/secret/) | |
service account	| A service account provides an identity for processes that run in a Pod. For more information on configuring the service accounts for Pods, [see Kubernetes Documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).	| | 
ClusterRole	| An RBAC Role or ClusterRole contains rules that represent a set of permissions. Permissions are purely additive (there are no "deny" rules). For more information on ClusterRole, [see Kubernetes Documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).	 | |
ClusterRoleBinding | A role binding grants the cluster-wide permissions defined in a role to a user or set of users. For more information on ClusterRoleBinding, [see Kubernetes Documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). | | 
namespaces | Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces. For more information on Namespaces, [see Kubernetes Documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/.	| | 
 
