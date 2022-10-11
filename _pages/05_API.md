---
layout: default
title: API
permalink: /api/overview
type: pbl
week: 7
---
<!-- HTML table fragment for page -->
## APIs in this Sub Menu
> HTML, CSS, and JavaScript are the front-end of the API.  Python and API resource definitions are used for RESTful API definitions. Abstraction of Frontend and Backend code, the exchange of standard data format (JSON), and guidelines for exchange (REST) is a technique that saves a lot of time between developers.  Learning APIs is a highly recommended step for every developer trying to break into the world of tech.<html>

<script>

    function testButtonClick(city) {
        
        alert("yo momma!:  " + city);

        // prepare HTML result container for new output
        const resultContainer = document.getElementById("astronomy");

        alert("1: " + resultContainer);

        // prepare fetch options
            const url = "https://weatherapi-com.p.rapidapi.com/astronomy.json";

alert("2: " + url);

/*
            
            const headers = {
                method: 'GET', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'omit', // include, *same-origin, omit
                headers: {
                    'Content-Type': 'application/json'
                    // 'Content-Type': 'application/x-www-form-urlencoded',
                    'X-RapidAPI-Key': '0b6ef107f7msh5606de624633ceap17521ejsn27566d20ff5b',
                    'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
                },
            };



        // fetch the API
        fetch(url, headers)
        // response is a RESTful "promise" on any successful fetch
        .then(response => {
            // check for response errors
            if (response.status !== 200) {
                const errorMsg = 'Database response error: ' + response.status;
                console.log(errorMsg);
                const tr = document.createElement("tr");
                const td = document.createElement("td");
                td.innerHTML = errorMsg;
                tr.appendChild(td);
                resultContainer.appendChild(tr);
                return;
            }
            // valid response will have json data
            response.json().then(data => {
                console.log(data);
                console.log(data.location)

                // World Data
                document.getElementById("name").innerHTML = data.location.name;
                document.getElementById("region").innerHTML = data.location.region;
                document.getElementById("country").innerHTML = data.location.country;
                document.getElementById("lat").innerHTML = data.location.lat;
                document.getElementById("lon").innerHTML = data.location.lon;
                document.getElementById("tz_id").innerHTML = data.location.tz_id;
                document.getElementById("localtime_epoch").innerHTML = data.location.localtime_epoch;
                document.getElementById("localtime").innerHTML = data.location.localtime;
*/

        /*
                // Country data
                for (const row of data.countries_stat) {
                    console.log(row);

                    // tr for each row
                    const tr = document.createElement("tr");
                    // td for each column
                    const name = document.createElement("td");
                    const cases = document.createElement("td");
                    const deaths = document.createElement("td");
                    const active = document.createElement("td");

                    // data is specific to the API
                    name.innerHTML = row.country_name;
                    cases.innerHTML = row.cases; 
                    deaths.innerHTML = row.deaths; 
                    active.innerHTML = row.active_cases; 

                    // this builds td's into tr
                    tr.appendChild(name);
                    tr.appendChild(cases);
                    tr.appendChild(deaths);
                    tr.appendChild(active);

                    // add HTML to container
                    resultContainer.appendChild(tr);
                }
            })
        })
        */

    }


</script>

<body>

<h1>API Information and Example</h1>

<a href="#overviewbutton"><button> Overview </button></a>
<a href="#astronomybutton"><button> Astronomy API </button></a>


<div id="overviewbutton">&nbsp;</div>

    <div>
        <hr>
        <p>
            A Web API is an application programming interface typically for a web browser.  Non-changing or Static Endpoints are used in interacting with the server-side Web APIs.  RESTful Web APIs use HTTP methods to access resources via URL parameters, and use JSON for transmitting text between client and server.
            <ul>
                <li>Server.  In these examples, we will be using Python to define REST APIs. Python tools are very popular for building RESTful APIs</li>
                <ul> 
                    <li>REST: Representational State Transfer.  A set of guidelines on how to architect a network-connected software system.</li>
                    <li>Client-server: One guideline is a client and server must be decoupled from each other, allowing each to develop independently.</li>
                    <li>Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or using authentication. This will be clarified by application and security requirements.</li>
                </ul>

                <li>Client.  JavaScript is the frontend language used to consume data from the Python defined REST APIs. Fetch will be used to make HTTP requests, as well as handle HTTP response.  There are four basic HTTP methods, they align with Create, Read, Update, Delete (CRUD).</li>
                <ul> 
                    <li>GET => Retrieve/Read data</li>
                    <li>POST => Create data</li>
                    <li>PUT => Update data</li>
                    <li>DELETE => Delete data</li>
                </ul>

                <li>REST endpoints will have similarity from application to application.  In planning APIs, for a Users system you can anticipate key methods.  The Users RESTful APIs would likely contain these endpoints.</li>
                <ul> 
                    <li>GET: /users => Get a list of users</li>
                    <li>GET: /users(id) => Get a single user</li>
                    <li>POST: /users => Create a new user</li>
                    <li>PUT: /users(id) => Update a user</li>
                    <li>DELETE: /users(id) => Delete a user</li>
                </ul>

                <li>Once a RESTful API receives and processes an HTTP request, it will return an HTTP response. Included in this response is an HTTP status code.  Common status codes are shown.</li>
                <ul> 
                    <li>200 => OK, this response will then have the promise of JSON data</li>
                    <li>400 => Bad Request</li>
                    <li>404 => Not Found</li>
                    <li>500 => Internal Server Error (aka bug)</li>
                </ul>

            </ul>
        </p>
        <hr>
    </div>

<!-- HTML table fragment for page -->


If you choose a city, it will list out the location and astronomy details.

<div id="astronomybutton">

<a href="#" class="btn btn-primary">Frontend Code!</a>
<a href="https://github.com/jesa06/andafp/blob/f5ded5f90611be9291c8ffe45f696a5e8b42e9b8/_notebooks/2022-10-03-PBL-python_rapidapi.ipynb" class="btn btn-primary">Backend Code!</a><br>

<label for="city">Enter city name:</label>
<input type="text" id="city" name="city">&nbsp;&nbsp;<input type="button" value="Get Location & Astronomy" onclick="testButtonClick(document.getElementById('city').value)">
<br><br>

<table>
  <thead>Location Details
  <tr>
    <th>City</th>
    <th>Region</th>
    <th>Country</th>
    <th>Latitude</th>
    <th>Longitude</th>
    <th>Time Zone</th>
    <th>Local Time Epoch</th>
    <th>Local Date and Time</th>
  </tr>
  </thead>
  <tbody>
    <td id="name"></td>
    <td id="region"></td>
    <td id="country"></td>
    <td id="lat"></td>
    <td id="lon"></td>
    <td id="tz_id"></td>
    <td id="localtime_epoch"></td>
    <td id="localtime"></td>
  </tbody>
</table>






<table>
    <thead>Astronomy Details
    <tr>
        <th>Sunrise</th>
        <th>Sunset</th>
        <th>Moonrise</th>
        <th>Moonset</th>
        <th>Moon Phase</th>
        <th>Moon Illumination</th>
    </tr>
    </thead>
    <tbody>
        <td id= "astronomy"></td>
    </tbody>
</table>    


</body>


<script>


/*
import requests

url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

city = input("Choose a city")
querystring = {"q":city}

headers = {
	"X-RapidAPI-Key": "0b6ef107f7msh5606de624633ceap17521ejsn27566d20ff5b",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json)

print("Location details")
loc = response.json().get('location')  // turn response to json() so we can extract "world_total"
for key, value in loc.items():  // this finds key, value pairs in country
    print(key, ":", value)

print()

// This code looks for USA in "countries_stats"
print("Astronomy details")
astro = response.json().get('astronomy') // countries is the key, countries_stat is the value
// print(astro.items())
for key, value in astro.items():
	for x in value.keys() :
		print(x, ":", value[x])

//astro in astronomy:  # countries is a list
    //print(astro)
*/

<script>