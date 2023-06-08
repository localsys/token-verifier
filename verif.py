import asyncio
import datetime
import io
import json
import os
import sys
import urllib.parse
import urllib.request
import time
from json import loads, dumps
from urllib import parse, request
from urllib.request import urlopen
import aiohttp
import colorama
import requests
from colorama import Fore, Style, Back
def read_json(filename):
    with open(f"{filename}", "r") as f:
        datajson = json.load(f)
    return datajson
def tokenverif():
    token = input("""Veuillez entrer votre token :  """)
    headers={
        'Authorization': token
    }
    connexion = requests.post('https://discordapp.com/api/v9/auth/login', headers=headers)
    if connexion.status_code == 200:
        print(Fore.GREEN + '[+] VALIDE' + ' ' + token)
    if connexion.status_code == 429:
        print(Fore.YELLOW + "[~] RATELIMIT, veuillez relancer le script.")
    if connexion.status_code == 400:
        print(Fore.RED + '[-] INVALIDE' + ' ' + token)
    if connexion.status_code == 403:
        print(f"{Fore.YELLOW} [~] Token Valide mais verouillé.")
    if connexion.status_code:
        print(f"[~] CODE DE CONNEXION {connexion.status_code}")
def tokensverif():
    tokens = read_json("tokens.json")
    tokens = tokens["tokens"]
    if tokens == []:
        print("Vous n'avez insere aucun token dans tokens.json")
        sys.exit(0)
    for tokens in tokens:
        headers={
        'Authorization': tokens
    }
        connexion = requests.post('https://discordapp.com/api/v9/auth/login', headers=headers)
        if connexion.status_code == 200:
            print(Fore.GREEN + '[+] VALIDE' + ' ' + tokens)
        if connexion.status_code == 400:
            print(Fore.RED + '[-] INVALIDE' + ' ' + tokens)
        if connexion.status_code == 403:
            print(f"{Fore.YELLOW} [~] Token Valide mais verouillé." + tokens)
        if connexion.status_code:
            print(f"[~] CODE DE CONNEXION {connexion.status_code}")
        

def supprimetokens():
    with open("tokens.json") as f:
        data = json.load(f)
        for tokens in data:
            data["tokens"] = []
            with open("tokens.json", "w") as f:
                json.dump(data, f, indent=4)
    print("Tous les tokens dans tokens.json ont été éffacés.")
def logo():
    print(f'''


{Fore.LIGHTBLUE_EX}  ______ ______ _____  
{Fore.LIGHTBLUE_EX} |____  |____  |  __ \ 
{Fore.LIGHTBLUE_EX}     / /    / /| |__) |
{Fore.LIGHTMAGENTA_EX}    / /    / / |  ___/ 
{Fore.LIGHTMAGENTA_EX}   / /    / /  | |     
{Fore.LIGHTMAGENTA_EX}  /_/    /_/   |_|     

Vérifieur de token discord (pour utilisateur)
{Fore.BLACK}
{Back.WHITE}ATTENTION CE N'EST PAS UN VERIFIEUR DE TOKEN POUR BOT{Back.RESET}
{Fore.LIGHTMAGENTA_EX}Je ne suis point responsable pour les dégats qui pourraient être causés par ce programme

Si le code de connexion est de :
401
404
405
5xx
Veuillez signaler ça sur mon github

codé par handy77p sur tous les reseaux (localsys sur github)
''')
logo()
r = input(f"""
{Fore.LIGHTBLUE_EX}[0] QUITTER LE PROGRAMME
{Fore.LIGHTMAGENTA_EX}[1] VERIFIER UN SEUL TOKEN
{Fore.LIGHTBLUE_EX}[2] VERIFIER PLUSIEURS TOKENS (tokens.json)
{Fore.LIGHTMAGENTA_EX}[3] EFFACER TOUS LES TOKENS DANS tokens.json
{Fore.LIGHTMAGENTA_EX}Faites votre choix :    """).lower()
if r == "1":
    print(f"""
{Fore.LIGHTBLUE_EX}Démarrage du vérifieur de token...
""")
    tokenverif()
if r == "2":
    print(f"""
{Fore.LIGHTMAGENTA_EX}Démarrage du vérifieur de tokens...
""")
    tokensverif()
if r == "0":
    sys.exit(0)
if r == "3":
    supprimetokens()
