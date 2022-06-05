import requests
import json

from HttpConnection.HttpMethods import HttpMethods


class HttpRequest:

    @staticmethod
    def send_request(uri, method, options):
        response = None
        methods = {HttpMethods.GET: requests.get,
                   HttpMethods.POST: requests.post,
                   HttpMethods.PUT: requests.put,
                   HttpMethods.DELETE: requests.delete}
        if not isinstance(options, dict):
            raise TypeError("Options should be of type dict")
        headers = options.get("headers", {})
        data = options.get("data", {})
        params = options.get("params", {})
        try:
            response = methods.get(method)(url=uri,
                                           headers=headers,
                                           params=params,
                                           data=json.dumps(data))
        except Exception as ex:
            print("Exception occurred: {}".format(ex))
        return response
