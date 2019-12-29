#!/bin/bash

for value in {2..1000}
do
    echo $value
    curl -k https://34.73.149.19/api/v1/users \
    -u "user1@email.com:Y1jU8cYmhpaNfkkdFkBBkroo8B0J9tS3" \
    -d "email=user$value@email.com" \
    -d "full_name=User $value" \
    -d "short_name=user$value" \
    -d "password=exemplo"
done

echo All done