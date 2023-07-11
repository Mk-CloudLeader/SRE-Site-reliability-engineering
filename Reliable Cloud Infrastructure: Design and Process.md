
# Reliable Cloud Infrastructure : Architecting, design, and process

A Cloud Architect's **job** is to determine which Cloud services to use in order to most effectively implement the applications and services they are building. The **starting point ** for any software development is to figure out what the software is supposed to do, who your users are, and why this is important. You will begin with this **requirements gathering phase**.

Once you understand your software's requirements and your users, you can start laying out the overall design. You need to consider your **compute** platform, **Storage** and **Database** requirements. Like do you want to deploy your apps to virtual machines, a Kubernetes cluster, or an automated platform, like App Engine. **Availability, durability, cost, and disaster recovery** are all important considerations when designing systems. 
Before implementing a system on Cloud, you should carefully consider its **security requirements** and use the appropriate security services.
At the **end**, you will **monitor** your app to see whether you're meeting your service objectives. These include dashboards, logs, error reporting, and tracing.

- Define services
- Microservice Design & Architecture
- DevOps Automation
- Choosing right storage Solutions
- Designing Reliable Systems
- Security
- Maintenance & Monitoring

## Microservice Design & Architecture - Microservices vs. monolithic architecture & Best Practices 

- Microservices
- Microservices Best Practices
- Activity : Designing Microservices for your applications
- Stateful services Vs stateless
- REST, API
- Activity :Designing REST API 
  
**What is Micoservice & difference from Monolithic applications?**

Microservices divide a large program into multiple smaller, independent services
Architecturally, a monolith or microservices should be modular components with clearly defined boundaries. With a monolith, the deployment is the grouping of the
components, whereas with microservices, the individual components are deployable.

**Stateful services have different challenges than stateless ones**
- Avoid storing shared state in-memory on your servers  => sticky sessions on your LB
- Store state using backend storage services shared by the frontend server (EFS, Firestore, Cloud SQL etc..) 

**REST API, loosely coupled applications**
- A good microservice design is loosely coupled. Clients shouldn’t need to know too many details of services they use
- Services communicate via HTTPS using text-based payloads
-   Client makes **GET, POST, PUT**, or **DELETE** request
-   Body of the request is formatted as **JSON** or **XML**
-   Results returned as **JSON, XML**, or **HTML**
-   **REST**(Representational State Transfer) architecture supports loose coupling
-     Protocol independent - **HTTP** is most common
- Service endpoints supporting REST are called **RESTful**
- RESTful services communicate over the web using HTTP(S)
- In REST, a client and server exchange representations of a resource. The **URI** provides access to a resource. Making a request for that resource returns a
representation of that resource, usually in JSON format.
- URI: Uniform Resource Identifier (endpoint)
![image](https://github.com/Mk-CloudLeader/SRE_Lab/assets/66654978/1b5b73f9-f98a-4eee-bba7-a8fdcaa75e84)

## Microservice Best Practices
-The Twelve-Factor App is a set of best practices for building web or software-as-a-service applications. Twelve-factor design helps you to decouple components of the application, so that each component can be replaced easily or scaled up or down seamlessly
  01. Codebase :
    - One codebase tracked in revision control, many deploys
    - Use a version control system like Git or SVN.
    - Each app has one code repo and vice versa.
  02. Dependencies :
      - Dependencies should be declared explicitly and stored in version control
      - Dependency tracking is performed by language-specific tools such as Maven for Java and Pip for Python.
      - Container Registry can be used to store the images
  03. Config   : Store config in the environment 
      - Don't put secrets, connection strings, endpoints, etc., in source code.
      - store those in the env variables 

  04. Backing Services :Treat backing services as attached resources
     - Databases, caches, queues,and other services are accessed via URLs.
      For example, when the app writes data to storage, treating the storage as a backing service allows you to seamlessly change the underlying storage type, because it's decoupled from the app. 
  6. Build, release, run :Strictly separate build and run stages
    - **Build** creates a deployment package from the source code.
     - **Release** combines the deployment with configuration in the runtime environment.
     - **Run** executes the application
  8. Processes  : Execute the app as one or more stateless processes
  9. Port binding  :Export services via port binding
  10. Concurrency  :Scale out via the process model
  11. Disposability
      - App instances should scale quickly when needed.  If an instance is not needed, you should be able to turn it off with no side effects.
  13. Dev/prod parity :Keep development, staging, and production as similar as possible
  14. Logs
      - Write log messages to standard output and aggregate all logs to a single source
  16. Admin processes  :Run admin/management tasks as one-off processes
      - Admin processes are usually one-off processes and should be decoupled from the application

## Deployment strategies :Canary|Blue/green|Rolling update|Traffic splitting

![image](https://github.com/Mk-CloudLeader/SRE_Lab/assets/66654978/4243e627-9df3-4385-9671-cbda1962209f)

**Canary deployment** is a deployment strategy where a new application release is introduced alongside the current release. This typically takes the form of percentage-based **traffic splitting**. For example - 10% to the new application release and 90% to the current release. Validation and testing is performed against the application, current and new.
### Diagrams  
WIP

**Blue/green** 
This is not tracffic spltting, In a blue/green deployment you perform **two** identical deployments of your application. Only one version is live at a time. Traffic is routed to the **blue deployment** while the **green deployment** is created and tested. After you're finished testing, you route traffic to the new version i.e - green deployment
After the deployment succeeds, you can either keep the **blue deployment** for a possible rollback or decommission it.

**Blue/green deployment Benefits:**
- Zero downtime
- Instant rollback
- Environment separation

  ### Diagrams        
WIP

  **Rolling update**




### Diagrams        



### Reference 
A|  
B| 
https://tanzu.vmware.com/content/blog/beyond-the-twelve-factor-app
https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
| Published  | Title/Link |
| ------------- | ------------- |
| Content Cell  | https://12factor.net |
| Content Cell  | https://cloud.google.com/architecture/twelve-factor-app-development-on-gcp  |

  
