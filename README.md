<div align="center">
<pre>
██████╗░██████╗░░█████╗░██████╗░░█████╗░████████╗██╗░░░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
██████╔╝██████╔╝██║░░██║██████╦╝███████║░░░██║░░░██║░░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██████╦╝██║░░██║░░░██║░░░╚██████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░
---------------------------------------------------
python cli program to test API endpoints
</pre>

</div>

It gets hectic testing so many API endpoints...
Here is a simple solution! Probatus -- A Python program that reads a json/yml file and tests api endpoints based on said expected values.

## Installation

pip install this repo.

```sh
pip3 install probatus
```

(or)

```sh
pip install probatus
```

## Usage example

### To get help with commandline arguments

```sh
probatus --help
```

### Using Command-line Arguments

```sh
probatus -f "some/folder/config.yml"
```

(or)

```sh
probatus -f "some/folder/config.json"
```

### Disclaimer

Sometimes the intallation does not work correctly. 

To fix this either run this temporarily or add to .zshrc:

```sh
export PYTHONPATH=/path/to/your/probatus/package:$PYTHONPATH
```

and then pip install.

Also, this program only works for get, post, put, delete, patch, and options requests. Will be adding more functionality in the future.

## Example config file (`config.yml`)

```yaml
environment:
  base_url: "https://jsonplaceholder.typicode.com"
  headers:
    Content-Type: "application/json"
    Accept: "application/json"

tests:
  - name: "Test User Retrieval"
    endpoint: "/users/1"
    method: "GET"
    expected:
      status_code: 200
      response_body:
        id: 1
        name: "Leanne Graham"
        username: "Bret"
        email: "Sincere@april.biz"
        address:
          street: "Kulas Light"
          suite: "Apt. 556"
          city: "Gwenborough"
          zipcode: "92998-3874"
          geo:
            lat: "-37.3159"
            lng: "81.1496"
        phone: "1-770-736-8031 x56442"
        website: "hildegard.org"
        company:
          name: "Romaguera-Crona"
          catchPhrase: "Multi-layered client-server neural-net"
          bs: "harness real-time e-markets"

  - name: "Test User Creation"
    endpoint: "/users"
    method: "POST"
    body:
      name: "Jane Doe"
      username: "janedoe"
      email: "jane.doe@example.com"
      address:
        street: "1234 North Street"
        suite: "Apt. 101"
        city: "Nowhere"
        zipcode: "12345"
        geo:
          lat: "11.1111"
          lng: "22.2222"
      phone: "555-1234"
      website: "example.com"
      company:
        name: "Doe Enterprises"
        catchPhrase: "Empowering Seamless Solutions"
        bs: "empower seamless synergies"
    expected:
      status_code: 201
      response_body:
        id: 11
        name: "Jane Doe"
        username: "janedoe"
        email: "jane.doe@example.com"
        address:
          street: "1234 North Street"
          suite: "Apt. 101"
          city: "Nowhere"
          zipcode: "12345"
          geo:
            lat: "11.1111"
            lng: "22.2222"
        phone: "555-1234"
        website: "example.com"
        company:
          name: "Doe Enterprises"
          catchPhrase: "Empowering Seamless Solutions"
          bs: "empower seamless synergies"

  - name: "Test User Deletion"
    endpoint: "/users/1"
    method: "DELETE"
    expected:
      status_code: 200
      response_body: {}
```

## Development setup

Clone this repo and install packages listed in requirements.txt

```sh
pip3 install -r requirements.txt
```