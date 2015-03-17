Cloud computing is rapidly gaining the interest of service providers, programmers and the public as no one wants to miss the new hype. While there are many theories on how the cloud will evolve no real discussion on the programmability has yet taken place. In this project a programing language named objic is described, that enables programs to run in a distributed manner in the cloud. This is done by creating an object orientated syntax and interpretation environment that can create objects on various distributed locations throughout a network and address them in a scalable, fault tolerant and transparent way.

Cloud computing is seen to bring together many services that are provided through the "world wide computer". A trend to multifunctional environments is currently taking place on the operating system kernel level encouraged by new virtualization techniques (see XEN, VMware, OpenBox). On the other hand, on the highest level of abstraction, object orientated notations and ideas are mostly used. The general concept is that once the cloud provider is chosen, a lock-in to his techniques and libraries occurs. Service compatibility is then achieved by adding specific output filters to the program (see SOAP, REST), which emulate object usage. This results in that every Software as a Service (SaaS) provider creates his own format. Other programs then have to retrieve this information and parse it accordingly and create local object representations, if they want to communicate with this service. This creates many difficulties especially when the format has to change. By these methods, both ends of a cloud service stack have become scalable, or in a nutshell "cloud enabled". Since the important layer of compilers and interpreters and as such the program constructs, have been neglected in the past few years, it is still the case that to use other services of a cloud provider, the programmer has to include some specific library or write the interface himself. Efforts to make compilers and/or interpreters more "cloud friendly" have only resulted in non-complete products and are not generally used. As seen by the success in the usage of SOAP and the object orientated paradigm, an object oriented distribution approach bears many advantages for the cloud, but has not been implemented in the layer of programming languages yet.

The project tries to introduce a novel object orientated programming language that acts as a layer of glue between the hardware cloud providers and the presentation of the user interface where object are already emulated and used. It should be possible to use an array of services provided in the cloud, through published objects, in an independent transparent way. It should further encourage people to offer a service to other users, through letting other people instantiate the objects they have written. In the current situation, if someone has written a good encryption library, for example, he is forced to use non standard methods to write a web service that makes this library usable. By using the language introduced in this project, publishing this library through a well defined interface and securing the intellectual property by keeping all execution in the server, should be enabled and encouraged. A further aim is to make it easy to incorporate services provided by different providers in a scalable, fault tolerant and traceable way. Despite that no attempt, known to the author, has been made so far to implement anything in this way.