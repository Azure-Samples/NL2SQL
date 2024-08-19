import requests
import json
import os
import re


def parse_query(response_content):
    # Extract the SQL query using regular expressions
    query = response_content["sql_query"].replace("```sql", "").replace("```", "")
    # Extract the table part
    table_content = response_content["database_output"]

    return query, table_content


class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_response(self, query, chat_history=[]):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

        data = {"question": query, "chat_history": chat_history}

        response = requests.post(self.base_url, json=data, headers=headers)
        response.raise_for_status()

        return response.json()

    def get_response_formatted(self, query, chat_history=[]):
        response = self.get_response(query, chat_history)
        query, table = parse_query(response)
        return query, table
