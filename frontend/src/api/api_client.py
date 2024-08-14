import requests
import json
import os
import re


def parse_query(response_content):
    # Extract the SQL query using regular expressions
    query_match = re.search(
        r"SQL Query:\s*```sql\s*(.*?)\s*```", response_content, re.DOTALL
    )
    query = query_match.group(1) if query_match else ""

    # Extract the table part
    table_match = re.search(r"Database Output:\s*\n\n(.*)", response_content, re.DOTALL)
    table_content = table_match.group(1) if table_match else ""

    # Split the table content into lines
    table_lines = table_content.strip().split("\n")

    # Extract headers
    headers = [header.strip() for header in table_lines[0].split("|") if header.strip()]

    # Extract rows
    rows = []
    for line in table_lines[2:]:  # Skip the header and separator lines
        values = [value.strip() for value in line.split("|") if value.strip()]
        row = dict(zip(headers, values))
        rows.append(row)

    return query, rows


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

    def parse_response(self, response_content):
        return parse_query(response_content)
