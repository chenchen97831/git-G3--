{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import os, sys\
\
def check_word_count(draft_path, max_words=100):\
    with open(draft_path, 'r', encoding='utf-8') as f:\
        text = f.read()\
    word_count = len(text.replace(" ", "").replace("\\n", ""))\
    if word_count > max_words:\
        print(f"Error: \{draft_path\} \uc0\u23383 \u25976 \u36229 \u27161  (\{word_count\}/\{max_words\})")\
        sys.exit(1) # \uc0\u22577 \u37679 \u65292 \u35320 \u30332 \u31934 \u28310 \u36864 \u22238 \
    print("Word count check passed.")}