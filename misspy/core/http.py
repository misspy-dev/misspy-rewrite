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
        """addressで指定されたサーバーにPOSTリクエストを送信します。

        Args:
            endpoint (str): エンドポイント (例: notes/create)
            data (dict): 送信するデータ。トークン(i)は自動的に挿入される為不要です。
            header (Union[str, None], optional): ヘッダー。ファイルが添付されている場合は利用されません。 Defaults to None.
            file (_type_, optional): ファイル。 Defaults to None.

        Raises:
            MisskeyAPIError: 何らかの理由でMisskeyAPIからエラーが返された場合発生します。

        Returns:
            dict: リクエスト結果
        """
        if header is None:
            header = self.header
        if self.i is not None:
            data["i"] = self.i
        if file is not None:
            resp = await self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data)
        else:
            resp = await self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data, headers=header)
        if not resp.status_code == 200:
            try:
                raise MisskeyAPIError(await resp.json())
            except:  # noqa: E722
                raise MisskeyAPIError(await resp.text())
        try:
            return await resp.json()
        except:  # noqa: E722
            return True

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
        if file is not None:
            resp = self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data)
        else:
            resp = self.session.post("http" + self.urlfmt + self.address + "/api/" + endpoint, data=data, headers=header)
        if not resp.status_code == 200:
            try:
                raise MisskeyAPIError(resp.json())
            except requests.exceptions.JSONDecodeError:
                raise MisskeyAPIError(resp.text)
        return resp.json()