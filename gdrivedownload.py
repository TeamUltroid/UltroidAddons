#Code Written By Senku Inspired From Darkcobra Plugin

"""
✘ Commands Available
• `{i}gdl`
    Show Fake Promotion
"""

import requests
import asyncio
import os
import sys


async def download_file_from_google_drive(id):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = await get_confirm_token(response)
    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    headers = response.headers
    content = headers['Content-Disposition']
    destination = await get_file_name(content)    

    file_name = await save_response_content(response, destination) 
    return file_name   

async def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

async def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return destination            

async def get_id(link): # Extract File Id from G-Drive Link
    file_id = ""
    c_append = False
    if link[1:33] =="https://drive.google.com/file/d/":
        link = link[33:]
        fid = ""
        for c in link:
            if c =="/":
                break
            fid = fid + c
        return fid     
    for c in link:
        if c == "=":
            c_append=True
        if c == "&":
            break
        if c_append:
            file_id = file_id + c
    file_id = file_id[1:]
    return file_id   

async def get_file_name(content):
    file_name = ""
    c_append = False
    for c in str(content):
        if c == '"':
            c_append = True
        if c == ";":
            c_append = False    
        if c_append:
            file_name = file_name + c
    file_name = file_name.replace('"',"")            
    print("File Name: "+str(file_name))
    return file_name                 

@ultroid_cmd(pattern=f"gdl")
async def g_download(ult):
    if ult.fwd_from:
        return   
    drive_link = ult.text[4:]
    print("Drive Link: "+drive_link)
    file_id = await get_id(drive_link)
    await ult.edit("Downloading Requested File from G-Drive...")
    file_name = await download_file_from_google_drive(file_id)
    await ult.edit("File Downloaded.\nName: `"+str(file_name)+"`")
            
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.H NDLR)}"})
  