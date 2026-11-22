{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import re, sys\
\
WHITELIST_DOMAINS = ["wikimedia.org", "gov.tw"]\
\
def check_links(html_path):\
    with open(html_path, 'r', encoding='utf-8') as f:\
        content = f.read()\
    \
    urls = re.findall(r'href="([^"]+)"|src="([^"]+)"', content)\
    for url_tuple in urls:\
        url = url_tuple[0] or url_tuple[1]\
        if url.startswith('http') and not any(domain in url for domain in WHITELIST_DOMAINS):\
            print(f"Error: \uc0\u20597 \u28204 \u21040 \u38750 \u30333 \u21517 \u21934 \u22806 \u37096 \u36899 \u32080  \{url\}")\
            sys.exit(1)\
    print("External links check passed.")}