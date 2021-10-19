#!/bin/bash
#
# Usage: run.sh
#
echo "STARTING Docker Flask Web"
chmod u+x *.sh
nohup snowflake_start_server --port=8910 --dc=1 --worker=1 >>/logs/snowflake-detail.log 2>&1 &
python app.py