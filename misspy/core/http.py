"""
This is the core library of misspy. Direct use is not recommended!
"""
from typing import Union

import aiohttp
import requests

from .exception import MisskeyAPIError

class AsyncHttpHandler:

    def __init__(self, address: str, i: Union[str, None]=None, ssl=True) -> None:
        self.i = i
        self.address = address
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.header = {"Content-Type": "application/json"}
        self.urlfmt = "://"
        if ssl:
            self.urlfmt = "s://"

    async def send(self, endpoint: str, data: dict, header: Union[str, None]=None, file=None) -> dict:
        if header is None:
            header = self.header
        if self.i is not None:
            data["i"] = self.i
        if not file is None:
            resp = await self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data)
        else:
            resp = await self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data, headers=header)
        if not resp.status_code == 200:
            try:
                raise MisskeyAPIError(await resp.json())
            except:
                raise MisskeyAPIError(await resp.text())
        return await resp.json()

class HttpHandler:

    def __init__(self, address: str, i: Union[str, None]=None, ssl=True) -> None:
        self.i = i
        self.address = address
        self.session = requests.Session()
        self.header = {"Content-Type": "application/json"}
        self.urlfmt = "://"
        if ssl:
            self.urlfmt = "s://"

    def send(self, endpoint: str, data: dict, header: Union[str, None]=None, file=None) -> dict:
        if header is None:
            header = self.header
        if self.i is not None:
            data["i"] = self.i
        if not file is None:
            resp = self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data)
        else:
            resp = self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data, headers=header)
        if not resp.status_code == 200:
            try:
                raise MisskeyAPIError(resp.json())
            except requests.exceptions.JSONDecodeError:
                raise MisskeyAPIError(resp.text)
        return resp.json()