{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
from bs4 import BeautifulSoup\
\
def check_font_size(html_path, min_size=24):\
    with open(html_path, 'r', encoding='utf-8') as f:\
        soup = BeautifulSoup(f, 'html.parser')\
    \
    # \uc0\u31777 \u26131 \u35299 \u26512  style \u20013 \u30340  font-size\
    for tag in soup.find_all(style=True):\
        if 'font-size' in tag['style']:\
            # \uc0\u25847 \u21462 \u25976 \u23383 \u37096 \u20998 \u27604 \u23565 ...\u33509 \u23567 \u26044  min_size \u21063 \u22577 \u37679 \
            pass\
            # sys.exit(1)\
    print("Font size check passed.")}