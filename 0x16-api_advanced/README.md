#	Project 0x16. API advanced

## Resources:
* [Reddit API Documentation](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA)
* [Query String](https://intranet.hbtn.io/rltoken/KtHEZIjOvJXYtufkJE1r4A)


## General Learning Objectives:

### How to read API documentation to find the endpoints youre looking for:
The endpoints indicate how you access the resource, while the method indicates the allowed interactions (such as GET, POST, or DELETE) with the resource.

The same resource usually has a variety of related endpoints, each with different paths and methods but returning different information about the same resource. Endpoints usually have brief descriptions similar to the overall resource description but shorter. Also, the endpoint shows the end path of a resource URL only, not the base path common to all endpoints.

### How to use an API with pagination:
Most endpoints that returns a list of entities will need to have some sort of pagination.

Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic.

Paging requires an implied ordering. By default this may be the items unique identifier, but can be other ordered fields such as a created date

### How to parse JSON results from an API:


### How to make a recursive API call:

### How to sort a dictionary by value:
