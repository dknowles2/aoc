#!/bin/bash

session="$HOME/.aoc-session"
usage="Usage: fetch_input.sh YEAR DAY"

if [[ ! -f "${session}" ]]; then
   echo "Please add your AoC session cookie to ${session}" >&2
   exit 1
fi

if [[ -z "$1" || -z "$2" ]]; then
    echo $usage >&2
    exit 1
fi

curl "https://adventofcode.com/$1/day/$2/input" \
  -H 'authority: adventofcode.com' \
  -H 'cache-control: max-age=0' \
  -H 'user-agent: AoCInputFetcher/1.0' \
  -H 'accept: text/html' \
  -H "referer: https://adventofcode.com/$1/day/$2" \
  -H 'accept-language: en-US,en;q=0.9' \
  -H "cookie: session=$(cat ${session})" \
  -s \
  --compressed > ${1}/input/day${2}.txt
