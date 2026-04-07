#!/bin/sh
export $(grep -v '^#' "$(dirname "$0")/.env" | xargs)
