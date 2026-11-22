{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import re, sys\
\
def check_sources_exist(draft_path):\
    with open(draft_path, 'r', encoding='utf-8') as f:\
        text = f.read()\
    \
    # \uc0\u27298 \u26597 \u27599 \u19968 \u27573 \u25110 \u27599 \u19968 \u38913 \u26159 \u21542 \u26377 \
    citations = re.findall(r'\\', text)\
    if not citations:\
        print(f"Error: \{draft_path\} \uc0\u32570 \u20047 \u20986 \u34389 \u27161 \u31844 \u65292 \u28041 \u23244 \u33258 \u34892 \u30332 \u26126 \u20839 \u23481 \u65281 ")\
        sys.exit(1)\
    # (\uc0\u36914 \u38542 \u65306 \u21487 \u21152 \u20837 \u27604 \u23565  cite \u27161 \u31844 \u26159 \u21542 \u30495 \u23526 \u23384 \u22312 \u26044  cards/ \u35041 )\
    print("Source check passed.")}