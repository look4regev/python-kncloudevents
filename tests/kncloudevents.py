#!/usr/bin/env python

"""
    Copyright 2019 The Elegant Monkeys

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import unittest
import json
from kncloudevents import kncloudevents
from cloudevents.sdk import marshaller
from cloudevents.sdk.event import v02
from cloudevents.sdk import converters
import requests
from multiprocessing import Process

m = marshaller.NewDefaultHTTPMarshaller()

event = (
    v02.Event().
        SetContentType("application/json").
        SetData({"name": "denis"}).
        SetEventID("my-id").
        SetSource("testing").
        SetEventType("cloudevent.event.type")
)

url = "http://localhost:8080"


def func(e):
    assert e.Data() == {"name": "denis"}


server = Process(target=lambda: kncloudevents.CloudeventsServer().start_receiver(func))


class TestKncloudevents(unittest.TestCase):
    """Tests for `kncloudevents` package."""

    @classmethod
    def setUpClass(cls):
        server.start()

    @classmethod
    def tearDownClass(cls):
        server.terminate()

    def test_structured(self):
        structured_headers, structured_data = m.ToRequest(event, converters.TypeStructured, json.dumps)
        requests.post(url, headers=structured_headers, data=structured_data.getvalue())

    def test_binary(self):
        binary_headers, binary_data = m.ToRequest(event, converters.TypeBinary, json.dumps)
        requests.post(url, headers=binary_headers, data=binary_data)
