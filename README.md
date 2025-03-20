# Simple System Inof
This is a projekt wich i used to get data of a machine using a webserver

## Usage

### Starting
```bash
python informer.py --port PORT --host HOST
```
``--port`` and ``--host`` is not needed

### Config
```json
{
    "tokens": [
        "TOKEN",
        "TOKEN2"
    ]
}
```
The tokens need to be given in the authorization header in a request.

### Example Request
```bash
curl -H "Authorization: TOKEN" http://HOST:PORT/sys/info/all
```
