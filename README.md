# Box_on_linux
Here are the instructions about how to setup box client on linux OS

## Step 1: create new App on Box Developers Console
1. [login](https://utexas.app.box.com/developers/console) your box account
2. Create New App -> Custome App -> User Authentication (OAuth 2.0)
3. Copy and save your Client ID and Client Secret (Recomend: saving to OS environment variables)
4. change 'Redirect URI' to 'http://localhost:4684'
5. save changes, (and request Box admins approval if necessary)

## Step 2: install box-python-sdk
```bash
pip install boxsdk
```

here is the [doc](https://github.com/box/box-python-sdk)

## Step 3: request access token and refresh token
1. run local http server with: 
```bash
python3 -m http.server 4684
```
2. run 
```bash
python3 get_box_token.py
```
3. this code would return you a URL, you should open it in browser
4. login and grant access (same as you login to Box), then it would redict to `localhost:4684`
5. you would see 
```
?state=box_csrf_token_#########&code=###############
```
6. copy the code and paste in the terminal where you are running `get_box_token.py`, press enter
7. now here are the access token and refresh token (it would be saved as `boxtoken.txt` in current directory, and valid for several days I think

## Step 4: fetch folder and files from Box with box client
1. run this and paste your access token and refresh token
```python
from BoxClient import BoxClient
boxclien = BoxClient
```
2. if you know the file or floder id, you can fetch the folder with 
```python
box_folder = boxclient.client.folder(folder_id=###)
```
or file with 
```python
box_file = boxclient.client.file(file_id=####)
```
The file or folder id could be found in your Box on browser

3. if you know the directory of the file in Box, then you can fetch the file recursively by fetching all items in current directory 
```python
items = box_folder.get_items()
```
and then find the target folder or file by `item.name`, finally you will find the target file and return `box_file=item`.

4. once you have the `box_file`, use wget to download it 
```python
wget.download(box_file..get_download_url(), your_directory)
```
5. for more instructions, read [doc for Box Api](https://developer.box.com/reference/)

