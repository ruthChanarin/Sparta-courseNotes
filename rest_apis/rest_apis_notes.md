# REST APIs Fundamentals


## HTTP 

Hypertext Transfer Protocol 

*an application layer protocol in the Internet protocol suit*

> facilitates communication between servers & apps for example 

**1.1** the most common version

-> when user enters URL, browser creates HTTP request & uses network to send it to server

-> server creates HTTP response, using network, to send it back to browser (interpreted/rendered by browser into visual content for user)


curl url    -> info about url

curl -v url (all info - v = verbose)

\> and < indicate direction of transfer (to or from)

Accept */* - to accept anything

> HTTP is **stateless** - closes after the request finishes (more like letters than phone calls)



## HTTP request

- HTTP Method
- version
- headers
- blank line

## HTTP response
- version
- status code
- headers
- blank line
- body of HTTP response (HTML or other kinds of text, Json XML, etc.)


## Important HTTP requests

- GET

- POST - to submit info

- PUT

- DELETE

- PATCH


### **HTTP.cat - HTTP status codes**


Number | Meaning
-------- | -------
100s | are waiting
200s |are okays
300s | url has relocated
400s | client side errors
500s | server side errors

> HTTPS = communication encrypted HTTP 
> clicking on the padlock by the url will > give you info about the privacy of this


# JSON 

the way objects are structured within JS

Can include numbers, strings, booleans, arrays (indexed sequence of values), JSON objects, null

We can store embedded JSON data structures within JSON data structures

data contained in {}

``` Javascript
	{
		“exchange-rate”: 12.07,
		“age”: 57,
		“charge”: -1.8e-19,
		“firstName”: “Neil”,
		“empty-string”: “”,
		“isTrainer”: true,
		“phoneNumbers”: [“12345”, “34567”, “84736”],
		“address”: {
			“street”: “123 High St”,
			“city”: “London”,
			“postcode”: “AD12 3FD”
		},
		“car”: null
	}
```

## Advantages

JSON is a compact data structure (no need for start & end stages like in XML files, which are therefore more verbose), also it reveals the data type by the form of entry (unlike in XML)

JSON arrays = a data structure which uses [] 



# REST API


> API = Application Programming Interface
	allows two computer programs to communicate with each other

> REST = Representational State Transfer
	an architectural style, not a standard (more of a strategy/approach)

> RESTful = complies with the REST architectural style


**Popular: flexible & applicable**

-> super easy to call from JS in webpages & from mobile apps to get data

-> also useful for the general integration of applications (with wide support for HTTP & JSON in programming languages)


## Constraints of REST (how to apply)

- client-server architecture
- statelessness
- cacheability (to avoid network traffic)
- layered system (clear interface with blackbox, encapsulated)
- uniform interface 
    - resource identification in requests, data format transferred not same as storage format
    - resource manipulation through representations
    - self-descriptive messages (through key elements of JSON)
    - hypermedia as the engine of application state (returns links)


## Typical REST technologies

- HTTP message exchange
- URIs - Uniform Resource Identifier & HTTP methods to describe location, actions & targets
- JSON to represent data (or possibly XML/HTML)
- Swagger/OpenAPI used to describe the service



## REST Implementation


CRUD describes how we often access data

 **C**reate

 **R**ead

 **U**pdate

**D**elete


> A REST API provides CRUD access to a datastore using HTTP as the transport & JSON as a way to represent the data


**Endpoint** = the URL we use to access an API

-> will communicate the HTTPS, host site, API, collection & specific element

## CRUD in REST

**CREATE  =  POST/PUT** (post used if doesn’t exist in DB; put updates if already exists)

**READ  =  GET**

**UPDATE  =  PUT/PATCH** (patch won’t insert, only update, put’ll insert)

**DELETE  =  DELETE**

can use query parameters to control the way in which data returns

- ie /per_page=2    limits to 2 pages

- &since=1000     only those after 1000


## Postman workspace

1. new collection
2. new request
3. name
4. fill in...


## HTTP Response Codes in REST APIs

Code | Response 
------ | -----
200 | OK
201 | Created
400 | Bad Request
401 | Unauthorized 
404 | Not Found
405 | Method Not Allowed
500 | Internal Server Error