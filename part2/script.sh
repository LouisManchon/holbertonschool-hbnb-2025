#!/bin/bash

echo -e "\n> Create New User:"
RESPONSE=$(curl -s -X POST http://localhost:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "Hugo", "last_name": "Chilemme", "email": "hugo.chilemme@example.com"}')
export USER="$(echo "$RESPONSE" | jq -r '.id')"
echo "User ID: $USER"

echo -e "\n> Update User:"
curl -X PUT http://localhost:5000/api/v1/users/$USER -H "Content-Type: application/json" -d '{"first_name": "Fabien", "last_name": "Chavonet", "email": "fabien.chavonet@example.com"}'

echo -e "\n> Get Users List:"
curl -X GET http://localhost:5000/api/v1/users/
